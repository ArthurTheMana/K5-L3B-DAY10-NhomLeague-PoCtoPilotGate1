# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomLeague
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Tài Minh Huy | 2A202603828 | Sản phẩm và kinh doanh |  |
|   2 | Hoàng Dương Anh Quân | 2A202603735 | Kỹ sư cổng |  |
|   3 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenTaiMinhHuy-2A202603828

### Phần việc phụ trách

Mình phụ trách chính thực hiện hai checkpoint đầu tiên của Lab 10, gồm thiết lập môi trường thực hành (CP1) và xây dựng, ký tiêu chí chấp nhận (CP2).

#### CP1 - Cài đặt và chia vai

Mình tạo repository bằng chức năng GitHub Template theo hướng dẫn ban đầu của Lab. Sau đó, mình clone repository về máy, cấu hình Git identity và thiết lập hai remote origin, upstream để quản lý source code.

Mình chạy bộ unit tests nhằm kiểm tra môi trường Python và các chức năng có sẵn. Khi giảng viên cập nhật repository, mình đồng bộ những file cần thiết và chạy lại các kiểm tra để bảo đảm hệ thống vẫn hoạt động bình thường.

#### CP2 - Ký tiêu chí (Phiếu A)

Mình hoàn thành các câu 1.1–1.6 trong templates/form-a-criteria.md, bao gồm:

- Xác định mục tiêu hệ thống AI Refund Assistant và nhu cầu của các bên liên quan.

- Thiết kế Offline Metric và Production Telemetry để đánh giá hành vi ghi lỗi hãng vận chuyển.

- Phân tích kết quả minh họa có khoảng tin cậy 95%.

- Xây dựng Acceptance Criteria với các ngưỡng chất lượng, an toàn và vận hành.

- Thiết lập quy tắc quyết định Gate 1 và điều kiện dừng.

- Điền config/acceptance_criteria.json và ký tiêu chí trước khi chạy Evaluation.

Sau khi ký, mình xác minh chữ ký, commit và push các file lên GitHub. Mình giữ nguyên Acceptance Criteria đã ký trong quá trình đồng bộ các thay đổi tiếp theo.

### Đóng góp cụ thể

| Checkpoint | Công việc | Kết quả |
|---|---|---|
| CP1 | Thiết lập GitHub repository và Git identity | Hoàn thành |
| CP1 | Clone repository, cấu hình remote và đồng bộ cập nhật | Hoàn thành |
| CP1 | Chạy Python unit tests | 13/13 PASS |
| CP2 | Hoàn thiện Phiếu A (A1–A5) | Đã điền |
| CP2 | Thiết lập Acceptance Criteria | Đã ký |
| CP2 | Xác minh tính toàn vẹn của tiêu chí | `ok: true` |
| CP2 | Kiểm tra Git history và push bằng chứng | Checker trả về `True`, đã push |

### Bằng chứng

- Repository: https://github.com/ArthurTheMana/K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1

- Các commit:

| Commit | Nội dung |
|---|---|
| `de8c1ab` | Ký Acceptance Criteria ban đầu |
| `5f6f534` | Hoàn thiện bằng chứng ký trong Phiếu A |
| `c18d831` | Đồng bộ cập nhật từ repository giảng viên |
| `ae95834` | Commit bổ sung đúng tên theo yêu cầu Git history checker, không thay đổi file tiêu chí |

- Kết quả kiểm tra:

Unit tests: 13/13 PASS.

Criteria verification: "ok": true.

Thời điểm ký: 2026-11-19T14:12:48.

- Git push: Thành công.

- Các file đã hoàn thiện:

templates/form-a-criteria.md

config/acceptance_criteria.json

config/acceptance_criteria.lock

### Exit ticket

#### Một điều mình học được:

Qua CP1 và CP2, mình hiểu rõ hơn sự khác biệt giữa một AI Agent chạy được trong môi trường thử nghiệm và một hệ thống đủ điều kiện triển khai thực tế.

Trước khi đánh giá, cần xác định rõ hệ thống phải đạt những tiêu chí nào, những rủi ro nào không được chấp nhận và cần làm gì khi kết quả không đạt. Việc ký Acceptance Criteria trước Evaluation cũng giúp quá trình đánh giá minh bạch hơn vì không thể tùy ý thay đổi ngưỡng sau khi đã nhìn thấy kết quả.

#### Một điều mình còn chưa chắc:

Mình vẫn chưa thật sự tự tin trong việc lựa chọn các ngưỡng Acceptance Criteria phù hợp với điều kiện vận hành thực tế. Chẳng hạn, Pass Rate 95% có đủ tốt hay không còn phụ thuộc vào mức độ nghiêm trọng của các lỗi và khả năng kiểm soát rủi ro.

Mình cũng muốn hiểu rõ hơn cách kết hợp Pass Rate, Pass^k, Safety Metrics và chi phí vận hành để đưa ra quyết định Go/No-go có căn cứ, thay vì chỉ dựa vào một chỉ số riêng lẻ.

## HoangDuongAnhQuan-2A202603735

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng** (phụ trách chính CP3 — Khối 2A, Khối 2B, chốt cổng vòng 1 và quyết định Gate 1 bản v1; đồng thời khởi tạo hồ sơ nộp bài trong `submission/submission.json`).

#### CP3 - Đo, tìm rủi ro, dựng cổng phòng ngừa vòng 1 và quyết định v1 (Phiếu B)

- Chạy đánh giá mốc baseline (`lab10.eval --suite base --stage base`), đối chiếu tiêu chí đã ký (`lab10.gate`) và dò trace lỗi `T-002@55` (`lab10.trace`).
- Hoàn thiện toàn bộ các mục **B0–B8** (câu 2.1–2.10 và quyết định v1) trong `templates/form-b-evaluation-gates.md`, kế thừa trực tiếp từ Bản tiêu chí đã ký ở Phiếu A (`e88a53d4`).
- Thiết kế và lập trình 3 cổng phòng ngừa cấp hệ thống trong `lab10/guards.py`:
  1. `pre_guard(ctx)`: ghim phiên bản chính sách hiệu lực theo ngày `as_of` (`H.effective_policy`).
  2. `write_gate` (`issue_refund`): chống hoàn trùng thực thời theo `ledger_rows`, đối chiếu quyền lợi từ tracking DB (`H.entitlement_vnd`), chặn `fail_open`, xác thực phê duyệt vượt hạn mức (`_valid_approval`), kiểm trần hoàn tự động khách/ngày và giữ đúng `payer == "LOGIX"`.
  3. `write_gate` (`file_carrier_fault` & `notify_carrier`): chống ghi trùng lỗi kiện hàng, xác thực `H.carrier_at_fault`, kiểm trần lỗi hãng/ngày, hiệu chỉnh về đúng `H.ticket_parcel` và lọc payload gửi hãng theo allowlist `carrier_notice_fields` để chặn rò rỉ PII.
- Cấu hình đầy đủ 3 nhóm cổng kinh doanh, vận hành và pháp lý trong `config/operating_gates.json` (khớp với Runbook phần 1–3 và kịch bản Giờ cao điểm).
- Thiết kế và chạy 2 behavioral test (`--adhoc`) kiểm chứng khả năng chống khai khống ngày trễ, prompt injection trừ tiền shop và rò rỉ PII đơn quà tặng.
- Chốt cổng vòng 1 (`python -m lab10.checkpoint`) tạo mốc `prepared`, chạy kiểm định `eval` + `gate` + 13/13 unit tests, và chốt quyết định **v1: Tiếp tục**.
- Điền thông tin phần vòng 1 vào `submission/submission.json` và chạy `lab10.check_submission --collect` để kiểm tra tiến độ bài nộp.

*Ghi chú sử dụng AI (`RULES.md`):* Có sử dụng trợ lý AI để hỗ trợ đọc codebase, gợi ý cấu trúc 3 cổng phòng ngừa tổng quát trong `lab10/guards.py` và soát câu chữ/tính nhất quán số liệu trong `templates/form-b-evaluation-gates.md`; mọi ngưỡng cấu hình, kết quả chạy lệnh và quyết định v1 đều được kiểm chứng trực tiếp bằng bộ công cụ `lab10.*`.

### Đóng góp cụ thể

| Checkpoint | Công việc | Kết quả |
|---|---|---|
| CP3 (2A) | Chạy baseline `base · base`, đối chiếu `lab10.gate` và dò trace `T-002@55` | Phát hiện lỗi chìm hoàn sai 20.000đ & 1 lỗi hãng oan `VNX` |
| CP3 (2A) | Hoàn thiện phân tích dữ liệu & drift (`REFUND-v4`), HAZOP mở rộng, Checklist 9 nhóm có PIC, Pre-mortem 4 lăng kính | Hoàn thành mục B1–B6 |
| CP3 (2B) | Code 3 cổng phòng ngừa trong `lab10/guards.py` và cấu hình `config/operating_gates.json` | `base · after` đạt `110/110` (`pass_rate 1.0`, `pass_k 1.0`, 0 lỗi an toàn) |
| CP3 (2B) | Chạy 2 ticket hiểm behavioral test (`--adhoc` trên `O-1002` và `O-1026`) và unit tests công khai | Giữ vững tính chất trên cả 2 ticket; `13/13` unit tests PASS |
| CP3 (Chốt v1) | Chốt cổng vòng 1 (`lab10.checkpoint`), đo mốc `prepared` và điền quyết định Gate 1 v1 | Hash chốt `1f03ce85`; `lab10.gate` đạt 9/9 ngưỡng; quyết định v1: **Tiếp tục** |
| Nộp bài | Cập nhật `TEAM.md`, điền thông tin vòng 1 trong `submission/submission.json` và chạy `check_submission --collect` | Hoàn thành phần vòng 1, sẵn sàng cho vòng 2 (Phiếu C) |

### Bằng chứng

- Repository: https://github.com/ArthurTheMana/K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1

- Các commit:

| Commit | Nội dung |
|---|---|
| `7034e2c` | Hoàn thiện Phiếu B (`B0–B8`), cổng vòng 1 (`lab10/guards.py`, `config/operating_gates.json`) và chốt mốc `prepared` (`guards_round1.py`, `operating_gates.round1.json`, `round1.lock`) |
| `3079d93` | Đồng bộ merge nhánh `main` với cập nhật `TEAM.md` của thành viên |

- Mã lần chạy (`runs/journal.jsonl`):
  - `R-base-before-20261119-143358-bde05c` (`base · base`): `pass_rate 0.9909 ([0.9727, 1.0])`, `pass_k 0.9545`, hoàn sai `20.000đ`, lỗi hãng oan `1`, hỏng `T-002@55`.
  - `R-base-after-20261119-143555-5d092c` (`base · after`, cổng vòng 1): `pass_rate 1.0`, `pass_k 1.0`, `0đ` hoàn sai, `0` lỗi hãng oan, `0` lộ PII.
  - `R-base-after-20261119-143703-708bc7` (`base · after`, bổ sung chống trùng lỗi hãng & thứ tự kiểm `fail_open`): `pass_rate 1.0`, `pass_k 1.0`, `0` lỗi an toàn.
  - `R-base-prepared-20261119-143710-708bc7` (`base · prepared`, hash chốt `1f03ce85`): `pass_rate 1.0 ([1.0, 1.0])`, `pass_k 1.0`, chi phí `4.456đ/ticket`, `ROI 1.24`, `0` ca bị ùn, `vượt trần: không`, `lab10.gate` đạt 9/9 ngưỡng đã ký.

- Kết quả kiểm tra:
  - Unit tests (`unittest discover -s tests`): `13/13 PASS`.
  - Checkpoint verification (`lab10.checkpoint verify`): `"ok": true`, hash `1f03ce85`.
  - Criteria verification (`lab10.criteria verify`): `"ok": true`, hash `e88a53d4`.

- Các file đã hoàn thiện:
  - `templates/form-b-evaluation-gates.md` (B0–B8)
  - `lab10/guards.py` và bản chốt `lab10/guards_round1.py`
  - `config/operating_gates.json`, bản chốt `config/operating_gates.round1.json` và `config/round1.lock`
  - `submission/submission.json` (thông tin bàn, thành viên, `decision_v1`) và `TEAM.md`

### Exit ticket

#### Một điều mình học được:

Qua CP3, mình thấy rõ sức mạnh của việc đặt **cổng kiểm soát cấp hệ thống ngoài model** (`pre_guard`, `write_gate` và `config/operating_gates.json`): thay vì cố sửa prompt để mong LLM không tin số khách khai hay không dính prompt injection, ta ép mọi lệnh ghi không đảo ngược (`issue_refund`, `file_carrier_fault`, `notify_carrier`) phải đối chiếu trực tiếp với nguồn sự thật (tracking DB, sổ cái thực thời, chính sách hiệu lực theo `as_of`, allowlist trường gửi bên thứ ba) và giới hạn bởi trần kinh doanh/vận hành.

#### Một điều mình còn chưa chắc:

Mình vẫn muốn kiểm chứng thực tế cách các cổng vòng 1 và cấu hình nhân sự (`reviewers_on_shift`, `pilot_scope`, `review_sampling_pct`) chịu tải ra sao khi gặp sự cố đột biến ngoài bộ nền (như tải tăng gấp 3 giờ cao điểm, LLM 429 hàng loạt hoặc thay đổi chính sách ngày `2026-12-01` ở vòng 2 và bộ test ẩn), cũng như cách cân bằng tối ưu giữa siết cổng an toàn và không làm tăng quá mức tỉ lệ chuyển người duyệt.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
