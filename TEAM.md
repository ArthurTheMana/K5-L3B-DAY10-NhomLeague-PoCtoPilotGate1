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
|   1 | Nguyễn Tài Minh Huy | 2A202603828 | Kỹ sư cổng (Tạm thời) |  |
|   2 | Hoàng Dường Anh Quân| 2A202603735 |     |             |
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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
