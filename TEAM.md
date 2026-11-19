# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Tài Minh Huy | 2A202603828 | Kỹ sư cổng (Tạm thời) |  |
|   2 |           |      |     |             |
|   3 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## Nguyễn Tài Minh Huy - 2A202603828

### Phần việc phụ trách

Hiện tại mình phụ trách thực hiện CP1 và CP2 của Lab 10.

#### CP1 - Cài đặt và chia vai

Tạo repository bằng GitHub Template theo hướng dẫn ban đầu.

Clone repository về máy tính.

Thiết lập Git identity và các remote origin, upstream.

Kiểm tra môi trường Python và chạy unit tests.

Đồng bộ những thay đổi mới từ repository của giảng viên.

#### CP2 - Ký tiêu chí (Phiếu A)

Hoàn thiện các câu 1.1–1.6 trong templates/form-a-criteria.md.

Xác định mục tiêu hệ thống và các bên liên quan.

Thiết kế Offline Metric và Production Telemetry.

Phân tích kết quả có khoảng tin cậy 95%.

Thiết lập Acceptance Criteria, các ngưỡng an toàn và quy tắc quyết định Gate 1.

Điền config/acceptance_criteria.json.

Ký tiêu chí trước Evaluation, xác minh chữ ký và push lên GitHub.

### Đóng góp cụ thể

- Thiết lập môi trường thực hành Day 10 và kiểm tra kết nối GitHub.

- Chạy thành công 13/13 unit tests.

- Hoàn thiện Phiếu A với các nội dung A1–A5.

- Thiết lập các ngưỡng chất lượng, an toàn và vận hành cho AI Refund Assistant.

- Ký Acceptance Criteria, tạo file lock và xác minh chữ ký hợp lệ.

- Commit và push các file liên quan đến CP2.

- Cập nhật tài liệu và công cụ Lab theo những thay đổi mới từ giảng viên.

- Chạy lại unit tests và kiểm tra chữ ký sau khi cập nhật, bảo đảm các kiểm tra vẫn thành công.

### Bằng chứng

- Repository: https://github.com/ArthurTheMana/K5-L3B-DAY10-NhomLeague-PoCtoPilotGate1

- Các commit:

de8c1ab: Sign Gate 1 acceptance criteria.

5f6f534: Hoàn thiện bằng chứng ký trong Phiếu A.

c18d831: Đồng bộ các cập nhật Day 10 từ giảng viên.

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

Qua CP1 và CP2, mình hiểu rằng việc xây dựng một AI Agent không chỉ dừng ở việc hệ thống chạy được hoặc trả lời đúng. Trước khi triển khai thực tế, cần xác định rõ các tiêu chí đánh giá về chất lượng, bảo mật, chi phí và rủi ro. Mình cũng hiểu được vì sao Acceptance Criteria phải được ký trước khi chạy Evaluation, tránh việc thay đổi ngưỡng dựa trên kết quả đã biết.

#### Một điều mình còn chưa chắc:

Mình vẫn cần hiểu rõ hơn cách lựa chọn các ngưỡng Acceptance Criteria sao cho phù hợp với dữ liệu và điều kiện vận hành thực tế. Đặc biệt, mình muốn tìm hiểu thêm cách kết hợp Pass Rate, Pass^k và các chỉ số an toàn để quyết định một AI Agent đã sẵn sàng cho Pilot hay chưa.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
