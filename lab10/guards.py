"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits
"""
from . import helpers as H
from .tools import Verdict


def _valid_approval(ctx, approval_id: str | None, order_id: str, amount_vnd: int) -> bool:
    """Xác thực mã phê duyệt từ nguồn sự thật: đúng ticket, đúng đơn, còn hiệu lực, đủ hạn mức."""
    if not approval_id:
        return False
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    appr = rows[0]
    return (
        appr.get("status") == "valid"
        and appr.get("ticket_id") == ctx.ticket.get("ticket_id")
        and appr.get("order_id") == order_id
        and str(appr.get("expires_at") or "") >= str(ctx.as_of)
        and int(appr.get("max_vnd") or 0) >= amount_vnd
    )


def pre_guard(ctx):
    # Cổng 1 (Pre-mortem / Drift chính sách): ghim đúng phiên bản chính sách hiệu lực theo ngày as_of,
    # không phụ thuộc cờ index_active vốn có thể bị cập nhật chậm khi đổi phiên bản.
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is None:
        ctx.log("missing_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không tìm thấy chính sách hoàn tiền hiệu lực theo ngày hiện tại")
    return Verdict.allow(policy_id=pol["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is None:
        return Verdict.escalate("không tìm thấy chính sách hiệu lực tại bước ghi")

    # Cổng 2 (HAZOP issue_refund / Pre-mortem kỹ thuật & kinh doanh):
    # Đối chiếu quyền lợi với nguồn sự thật (tracking DB + chính sách hiệu lực), chống fail-open,
    # chống hoàn trùng thực thời, xác thực phê duyệt vượt hạn mức và trần hoàn tự động theo khách/ngày.
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.escalate("không tìm thấy đơn hàng trong nguồn sự thật khi hoàn tiền")

        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            ctx.log("duplicate_refund_blocked", order_id=order["order_id"])
            return Verdict.deny("đơn hàng đã có giao dịch hoàn tiền trong sổ cái")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        # Tracking records marked DELIVERED must carry a delivery date. Without it,
        # db_delay_days falls back to today's date and can invent a carrier strike.
        if parcel.get("status") == "DELIVERED" and not parcel.get("delivered_date"):
            ctx.log("carrier_fault_missing_delivery_date", order_id=order["order_id"],
                    parcel_id=parcel["parcel_id"], status=parcel.get("status"))
            return Verdict.escalate("tracking không nhất quán: kiện đã giao nhưng thiếu ngày giao; cần Ops xác minh")
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause")
        expected = H.entitlement_vnd(pol, order, db_delay, cause)

        if expected <= 0:
            ctx.log("refund_denied_by_db", order_id=order["order_id"], db_delay=db_delay,
                    asked=action.get("amount_vnd"), cause=cause)
            return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách hiệu lực")

        if action.get("basis") == "fail_open":
            ctx.log("blocked_fail_open_refund", order_id=order["order_id"])
            return Verdict.escalate("LLM lỗi khi kiểm tra chính sách (fail-open), chuyển người duyệt")

        approval_id = action.get("approval_id")
        if expected > pol["auto_limit_vnd"]:
            if not _valid_approval(ctx, approval_id, order["order_id"], expected):
                ctx.log("invalid_or_missing_approval", order_id=order["order_id"],
                        approval_id=approval_id, expected=expected)
                return Verdict.escalate("vượt hạn mức tự động và chưa có phê duyệt hợp lệ, chuyển người duyệt")
        else:
            cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
            if cust_cap is not None and not approval_id:
                spent_cust = sum(
                    r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                    if not r.get("approval_id")
                )
                if spent_cust + expected > cust_cap:
                    ctx.log("customer_daily_cap_exceeded", customer_id=order["customer_id"],
                            spent=spent_cust, expected=expected, cap=cust_cap)
                    return Verdict.escalate("vượt trần hoàn tự động mỗi khách/ngày, chuyển người duyệt")

        if action.get("amount_vnd") != expected or action.get("payer", "LOGIX") != "LOGIX":
            ctx.log("refund_corrected_to_db", asked=action.get("amount_vnd"),
                    expected=expected, asked_payer=action.get("payer"))
            return Verdict.modify(
                "điều chỉnh số tiền hoàn và bên chi trả về đúng nguồn sự thật (tracking DB + chính sách)",
                amount_vnd=expected,
                payer="LOGIX",
            )
        return Verdict.allow()

    # Cổng 3 (HAZOP file_carrier_fault & notify_carrier / Pre-mortem pháp lý — bên thứ ba):
    # Xác thực lỗi hãng theo đúng kiện hàng & nguyên nhân trong DB, kiểm trần lỗi hãng/ngày,
    # và chỉ cho phép gửi đúng danh sách trường tối thiểu (allowlist) nhằm ngăn rò rỉ PII.
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.deny("không tìm thấy đơn hàng để đối chiếu lỗi hãng")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
            ctx.log("duplicate_carrier_fault_blocked", order_id=order["order_id"], parcel_id=parcel["parcel_id"])
            return Verdict.deny("kiện hàng này đã được ghi nhận lỗi hãng trước đó")

        if not H.carrier_at_fault(pol, parcel, db_delay):
            ctx.log("carrier_fault_denied_by_db", order_id=order["order_id"],
                    parcel_id=parcel["parcel_id"], db_delay=db_delay, cause=parcel.get("delay_cause"))
            return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB và chính sách hiệu lực")

        strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if strike_cap is not None:
            strikes_today = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
            if strikes_today >= strike_cap:
                ctx.log("carrier_strike_cap_reached", carrier_id=parcel["carrier_id"],
                        strikes_today=strikes_today, cap=strike_cap)
                return Verdict.deny("hãng đã chạm trần lỗi tự động trong ngày, cần Ops xác minh thủ công")

        if (
            action.get("parcel_id") != parcel["parcel_id"]
            or action.get("carrier_id") != parcel["carrier_id"]
            or action.get("driver_id") != parcel.get("driver_id")
            or action.get("delay_days") != db_delay
        ):
            ctx.log("carrier_fault_corrected_to_parcel", old_parcel=action.get("parcel_id"),
                    new_parcel=parcel["parcel_id"], db_delay=db_delay)
            return Verdict.modify(
                "điều chỉnh lỗi hãng về đúng kiện hàng, hãng và số ngày trễ theo tracking DB",
                parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"],
                driver_id=parcel.get("driver_id"),
                delay_days=db_delay,
            )
        return Verdict.allow()

    if tool == "notify_carrier":
        allowed = set(pol.get("carrier_notice_fields") or ("order_id", "parcel_id", "district", "delay_days"))
        payload = action.get("payload") or {}
        cleaned = {k: v for k, v in payload.items() if k in allowed}
        if len(cleaned) != len(payload):
            dropped = sorted(set(payload) - set(cleaned))
            ctx.log("carrier_notice_pii_stripped", dropped=dropped)
            return Verdict.modify(
                "lọc thông báo gửi hãng chỉ giữ đúng trường tối thiểu theo chính sách, chặn rò rỉ PII",
                payload=cleaned,
            )
        return Verdict.allow()

    return Verdict.allow()
