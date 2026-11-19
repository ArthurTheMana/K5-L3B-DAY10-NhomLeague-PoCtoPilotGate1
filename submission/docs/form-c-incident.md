# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1 · **Thẻ đã bốc:** S1 *(thẻ bàn được giao)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S1-prepared-20261119-214126-f5f130` | S1 · prepared | Chỉ dùng cổng vòng 1 sau khi nhận thẻ | 0.7692 [0.5385; 1.0] | 0.7692 | 275.000đ · 5 · 0 | 0.1538 | Cổng vòng 1 giảm lỗi nhưng vẫn còn hoàn sai và strike oan. |
| 2 | `R-S1-after-20261119-222256-427bb7` | S1 · after | Chặn strike khi tracking thiếu ngày; monitor mới đã sáng | 0.9231 [0.7692; 1.0] | 0.9231 | 0đ · 0 · 0 | 0.3077 | Lỗi oan về 0; monitor incident=0.153846, base=0. |
| 3 | `R-S1-after-20261119-222254-427bb7` | S1 · after | Chạy eval sau sửa monitor | 0.9231 [0.7692; 1.0] | 0.9231 | 0đ · 0 · 0 | 0.3077 | Giữ an toàn, S1-07 còn lỗi. |
| 4 | `R-base-after-20261119-222255-427bb7` | base · after | Kiểm regression | 1.0 [1.0; 1.0] | 1.0 | 0đ · 0 · 0 | 0.2727 | Bộ nền 110/110, không ca mới hỏng. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S1-grade-20261119-222255-427bb7` · base: `R-S1-before-20261119-222255-427bb7` · prepared: `R-S1-prepared-20261119-222255-427bb7`
- Cổng vòng 1 giảm hoàn sai 985.000đ → 275.000đ và lỗi hãng oan 30 → 5; PII vẫn 0.
- Không có trần vận hành vượt; chi phí 3.656đ/ticket, ROI 0.58, hàng chờ tối đa 0 phút.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính kỹ thuật và con người/vận hành đối tác; hậu quả kinh doanh là nguy cơ phạt, đình tuyến.
- Pre-mortem đã nêu model tin lời khách/ghi lỗi oan; prepared giảm 25/30 lỗi. Bỏ sót tracking mâu thuẫn: DELIVERED nhưng thiếu delivered_date.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Parcel DELIVERED nhưng thiếu delivered_date làm helper suy độ trễ tới ngày hiện tại | Kỹ thuật/vận hành | parcel tracking và trace S1-20@11 |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** GHSH và 12 tài xế · wrongful_carrier_faults / tiền phạt · 30 lỗi oan ở base

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | S1-07@11: DB báo trễ 4 ngày, model_override dùng 2 ngày khách khai; agent từ chối hoàn 21.000đ | Khách C-14 | Cao | Lỗi ngữ cảnh/đầu vào |
| 2 | S1-20@11: DELIVERED, delivered_date=null; helper suy 6 ngày, hoàn và ghi GHSH lỗi | GHSH/khách | Cao | Lỗi chìm/dữ liệu thiếu |
| 3 | S1-40…43: nhiều strike GHSH dồn trong ngày, có nguy cơ kích hoạt đình tuyến | GHSH/tài xế | Cao | Vận hành |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | X — dùng số khách khai | — | — |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | — | X — thiếu ngày giao | — |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | — | — | X — cần đối soát sổ hãng |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | — | — | X — strike dồn theo ngày |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Khách mất quyền lợi | GHSH chịu strike vô căn cứ | Tuyến/tài xế bị ảnh hưởng |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Reviewer kiểm policy | Ops xác minh tracking | PIC đối soát GHSH |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Reviewer xác minh entitlement rồi trả lời khách | Ops xác minh parcel trước khi ghi lỗi | PIC so sổ hai bên và báo đối tác |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | model_override so DB | carrier_fault_missing_delivery_date_rate | wrongful_carrier_faults theo ngày |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | Có | Hoàn tiền; hợp đồng GHSH phạt 150.000đ/lỗi và đình tuyến sau 3 lỗi/7 ngày. |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | Có | GHSH yêu cầu rà trước 17h; 12 tài xế có nguy cơ nghỉ tuyến. |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | Có | Prepared còn 5 lỗi oan; visible pass_rate 0.7692. |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | Có | S1-20 có DELIVERED nhưng delivered_date=null, cần Ops xác minh. |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | Có | Tracking mâu thuẫn hoặc GHSH khiếu nại thì tạm dừng ghi, chuyển Ops. |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| Khách hàng/trợ lý | `issue_refund` dưới hạn mức tự động | Thấp nếu entitlement có căn cứ; vừa nếu dữ liệu mâu thuẫn | Tự động; sau sửa dữ liệu thiếu thì chuyển Ops | Chuyển người khi chưa đủ căn cứ |
| NV-HANH (Trần Thị Hạnh) | `issue_refund` trên hạn mức tự động | Cao | Yêu cầu approval hợp lệ và đủ hạn mức | Không lệch nếu hợp lệ; mã hết hạn thì escalate |
| NV-OANH (Phạm Kiều Oanh) | `issue_refund` mà người trả là shop | Cao | Gate chỉ cho payer LOGIX | Chặn debit shop; ngoại lệ chuyển Finance |
| NV-OANH và NV-TUNG | nhiều khoản hoàn tự động cho một khách trong ngày | Cao | Ledger và daily cap kiểm soát tổng | Dừng tự động nếu trùng/chạm trần, rà sổ |
| NV-TUNG (Lê Thanh Tùng) | `file_carrier_fault` khi parcel thiếu dữ liệu/nhiều strike | Cao | Sau sửa thiếu ngày thì escalate Ops | Ops xác minh, Oanh đối soát |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `Điều phối GHSH/tài xế` | Nhóm B: `Kế toán đối soát NV-OANH` |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | GHSH nhận strike/notice, chịu phạt và nguy cơ đình tuyến | Oanh đối soát sổ LogiX với GHSH hằng tuần |
| Mục tiêu chính của họ | Strike đúng kiện, đúng hãng, có chứng cứ | Sổ hai bên khớp trước khi tính phạt |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | So mã kiện, ngày hẹn/ngày giao, scan/chữ ký và chặng hãng quản lý | So tracking parcel với chứng từ GHSH, xác nhận carrier/cause |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Có thể khác theo depot/tài xế; email cho thấy sổ hai bên lệch | Chưa có bằng chứng các depot làm đồng đều; cần chuẩn hóa |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | Kiện/chặng; tài xế khi có chứng cứ | Kiện gắn với hãng, liên kết về đơn để đối soát |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `parcel`. Bằng chứng: ticket `S1-20@seed 11`, trace `file_carrier_fault` ghi `parcel_id=O-2120-P1`, carrier GHSH.
- Chỗ hai hình dung vênh nhau: hệ thống tự chọn parcel/delay từ tracking; GHSH cần chứng cứ theo chặng. DELIVERED nhưng thiếu ngày chưa đủ căn cứ quy lỗi.
- Khi đầu vào không đủ parcel_id, hệ thống có thể chọn parcel trễ nhất qua `ticket_parcel`; nên chuyển Ops, xác định kiện rồi mới quyết định ghi lỗi.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | Gửi yêu cầu trong app, nghĩ ghi chú chỉ LogiX đọc | `customer_note` có thể đi trong `notify_carrier` | Không biết ghi chú được gửi cho hãng |
| **Tin quá mức** | người nhận hàng | Nghĩ thông tin chỉ dùng cho giao nhận | Recipient nằm trong order; trace S1-20 có customer_note gửi hãng | Không dùng trợ lý và không được báo ticket note chuyển bên thứ ba |
| **Không tin** (sau sự cố) | người nhận hàng | Nếu hãng liên hệ lại về nội dung khiếu nại, mất tin tưởng LogiX | `customer_note`/district đến carrier | Không biết nơi nhận, thời hạn lưu của hãng |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Khách được báo dữ liệu gửi đi; người nhận chỉ có thông tin cần giao kiện | Payload tối thiểu theo policy | Khách biết mục đích; người nhận không lộ note khiếu nại |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `customer_note`, order_id/parcel_id/district/delay_days → `carrier:GHSH`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: chỉ gửi dữ liệu tối thiểu cần thiết; bỏ `customer_note` và PII.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: giảm khả năng; allowlist không ngăn bên nhận sao chép dữ liệu đã gửi.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | Thấy approval_id và tin căn cứ đã được kiểm | approval_id, max_vnd, expires_at | Có thể không thấy tracking thiếu ngày hoặc claim override |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | Tin trạng thái đã duyệt nghĩa là người có thẩm quyền xác minh | approval row, decision_note | Không thấy ai xác minh dữ kiện gốc |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | Audit thấy bản trước sửa S1-20 hoàn/ghi lỗi dù thiếu ngày | tracking/proposal/ledger/fault trace | Phải rà tay cả ca hợp lệ khác |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | Bị quy trách nhiệm về hoàn/strike sai | ticket_id, approval_id, decision_note, ledger | Không thấy nguồn dữ kiện và người xác nhận |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Có policy, tracking, số tiền/parcel và người duyệt rõ | Trace/ledger gắn ticket/order | Reviewer kiểm mẫu và có quyền dừng khi mâu thuẫn |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: approval_id/trạng thái duyệt tách khỏi ticket, tracking và lý do quyết định.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: 10% ca tự động; tăng 100% khi có cảnh báo, reviewer giữ quyền dừng/chuyển Ops. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `parcel.status`, `promised_date`, `delivered_date`, `delay_cause` | Tracking là nguồn sự thật, chưa kiểm tính nhất quán trường | DELIVERED có thể thiếu delivered_date; delay_cause có thể null | Không suy thiếu ngày thành trễ; sai cause/delay gây hoàn hoặc strike oan |
| `parcel_id`, `carrier_id`, `driver_id` | Nguồn sự thật, chưa phân tích đơn vị chịu lỗi | Mỗi kiện có carrier/tài xế riêng | Chọn sai parcel/carrier quy lỗi sai hãng/tài xế |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: HAZOP

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| delay_days | WRONG | S1-07@11: khách khai 2 ngày, DB ghi 4 | Khách bị từ chối quyền lợi, hãng có thể bị quy sai | Đối chiếu DB | Chỉ dùng DB; tầng chặn |
| delivered_date | INCOMPLETE | S1-20@11: status DELIVERED, ngày giao null | GHSH bị strike oan | Trước sửa chưa có | Chuyển Ops; tầng chặn |
| feed tracking | PERTURBED | Nhánh chưa thấy: feed cập nhật trễ so với sổ GHSH | Hãng/tài xế chịu lỗi sai | Chưa có | Đối soát timestamp với hãng; tầng vận hành |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Chỉ ghi strike khi parcel có ngày giao hợp lệ, delay thỏa policy và cause được policy cho phép.

Kiểm bằng `write_gate(file_carrier_fault)`; report ghi `wrongful_carrier_faults` (after = 0).

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định: tracking LogiX đồng bộ, đầy đủ và đúng với sổ giao thực tế của hãng.

Feed có thể trễ hoặc thiếu; S1-20 có status DELIVERED nhưng delivered_date=null.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S1-grade-20261119-214125-f5f130`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] GHSH bị ghi lỗi oan, có thể bị phạt/đình tuyến (cho ai: GHSH và 12 tài xế, đo bằng wrongful_carrier_faults/tiền phạt)
 └─ HOẶC
├─ [1] Model dùng số ngày khách khai thay DB tầng: đầu vào
│ └─ vì: claim được ưu tiên hơn tracking bằng chứng: ticket S1-07@seed 11
├─ [2] Thiếu ngày giao bị suy thành trễ tầng: data
│ └─ vì: DELIVERED nhưng delivered_date=null bằng chứng: ticket S1-20@seed 11
└─ [3] Strike dồn không được đối soát tầng: vận hành
└─ vì: có thể kích ngưỡng đình tuyến bằng chứng: 5 lỗi GHSH ở prepared
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Độ trễ phải lấy từ tracking DB | Giả định khách khai đúng đã sai (S1-07@11) |
| [2] | Không suy trễ khi delivered_date thiếu | Giả định tracking đủ trường đã sai (S1-20@11) |
| [3] | Strike cần đối soát trước áp phạt | Giả định sổ hai bên luôn đồng bộ có thể sai |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Tracking thiếu ngày giao | `write_gate/file_carrier_fault` | Chặn | Ngăn ghi nếu thiếu ngày; không ngăn DB sai đủ trường | R-S1-after-20261119-222256-427bb7 |
| [2] | Model override delay | So delay với DB trong `write_gate` | Chặn | Ngăn dùng số model khác DB | R-base-after-20261119-214125-f5f130 |
| [3] | Strike dồn trong ngày | Quy trình Ops/đối soát hãng | Vận hành | Giảm khả năng/tác động; cần người xác minh | R-S1-after-20261119-214124-f5f130 |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `carrier_fault_missing_delivery_date_rate` |
| **Bước / hành vi được đo** | Parcel DELIVERED thiếu ngày giao trước khi ghi lỗi hãng |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ trial có guard cảnh báo thiếu ngày giao (%) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events`: type=guard, kind=carrier_fault_missing_delivery_date |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Trial có cảnh báo / tổng trial; nếu mẫu số 0 trả 0 |
| **Khung thời gian / ngưỡng báo động** | Tổng hợp theo ngày; cảnh báo khi >0 |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không phát hiện tracking đủ trường nhưng giá trị sai |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | 0.0 · 0.153846 (monitor đã sáng đèn trên incident) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S1-grade-20261119-222255-427bb7`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] GHSH bị ghi strike oan
 └─ HOẶC
├─ [1] tracking thiếu ngày VÀ [gate file_carrier_fault bỏ lọt]
├─ [2] model override delay VÀ [gate so DB bỏ lọt]
└─ [3] tracking đủ trường nhưng sai (còn hở)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `write_gate` kiểm delivered_date | Chặn | Ngăn khi thấy thiếu ngày | DB sai nhưng đủ trường |
| [2] | Đối chiếu delay với DB | Chặn | Ngăn dùng số model | Tracking gốc sai |
| [3] | Đối soát với hãng | Vận hành | Giảm khả năng | Feed đủ trường nhưng sai |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tracking đủ trường nhưng sai khác sổ GHSH | Vừa | Cao: strike/phạt/đình tuyến | NV-TUNG | wrongful_carrier_faults >0 hoặc khiếu nại GHSH | Tạm dừng tự động ghi, đối soát | Có thể đổi quyết định Gate 1 | MEASURE/MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 7 · Vận hành | Chưa | Thêm cảnh báo tracking và đối soát carrier; mục C8 | NV-TUNG |
| 8 · Kiểm thử | Xong | Regression base 110/110; S1-07 còn hỏng | Hoàng Dương Anh Quân |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Có stop condition lỗi hãng, chưa có cảnh báo tracking thiếu ngày. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm cảnh báo `carrier_fault_missing_delivery_date_rate > 0`; wrongful faults giữ ngưỡng 0. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 reviewer; NV-TUNG điều phối, NV-HANH duyệt, gọi Ops khi tracking mâu thuẫn. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ pilot; đối soát strike với GHSH; nâng kiểm mẫu 10%→100% khi cảnh báo. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-TUNG báo GHSH trong 4 giờ, tạm dừng strike và gửi kết quả đối soát. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Report PII leak=0; trace S1-20 trước sửa có customer_note gửi hãng, báo Legal/PIC xác minh. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Phản hồi GHSH; thiếu feed đối soát độc lập và timestamp cập nhật tracking. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì: thu hẹp tiếp nhận và bổ sung reviewer.
2. Nếu nhà cung cấp LLM lỗi quá 5 phút thì: chuyển queue xử lý thủ công, không tự động ghi.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: dừng lệnh ghi và audit 100% ca trong ngày.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | S1 · base `R-S1-before-20261119-222255-427bb7` · prepared `R-S1-prepared-20261119-222255-427bb7` · after `R-S1-after-20261119-222256-427bb7` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không vượt trần; after hoàn sai 0, lỗi hãng oan 0, PII 0. |
| Kho hoặc hãng có số xấu nhất: HCM/VNX. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | HCM pass 0.6667; VNX 0/5. Mẫu nhỏ nhưng củng cố Cải tiến thêm. |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · **[Cải tiến thêm]** · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S1-grade-20261119-222255-427bb7`: pass_rate 0.9231 <0.95; pass_k 0.9231 ≥0.90. |
| Bằng chứng 2 | Hoàn sai 0đ, wrongful faults 0, PII 0; không vượt trần. |
| Bằng chứng 3 | Regression base 110/110; S1-07 còn hỏng. |
| Khớp dòng nào trong `decision_rule` đã ký? | Chưa đạt điều kiện Tiếp tục vì pass_rate bắt buộc chưa đạt. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không áp dụng. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Điều tra S1-07 và kiểm phân khúc; xem lại 2026-11-26. |
| Nếu Dừng: bài học ghi lại | Không áp dụng. |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-26 |
| PIC ký | Đại diện Sản phẩm và Ops của bàn |

**Chỉ ở v2**
- Đổi từ Tiếp tục sang Cải tiến thêm vì pass_rate 0.9231 <0.95.
- Report tự kiểm tra: `R-S1-grade-20261119-222255-427bb7` · integrity còn đỏ do MANIFEST khoá không khớp; pass_rate visible 0.9231 <0.95; S1-07 còn lỗi.
- Prepared giảm lỗi oan 30→5 và hoàn sai 985.000đ→275.000đ; bỏ sót tracking thiếu delivered_date.
- Report ghi không đủ căn cứ Tiếp tục; quyết định Cải tiến thêm khớp.
- Chưa đo độ đúng tracking production và tải cao điểm; cần đo trước Gate 2.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Tracking đủ và cập nhật đúng hạn; production có thể trễ hoặc sai.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Ngăn ghi strike nếu thiếu ngày giao; chỉ giảm rủi ro tổng thể vì tracking đủ trường vẫn có thể sai.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Đối chiếu strike với sổ hãng, đo tracking thiếu/sai ngày và pass_rate theo kho/hãng.


