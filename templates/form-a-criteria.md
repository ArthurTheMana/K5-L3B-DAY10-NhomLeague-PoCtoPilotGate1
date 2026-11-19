# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Mục tiêu của hệ thống là hỗ trợ xử lý yêu cầu hoàn tiền do giao hàng trễ một cách chính xác, an toàn và có thể kiểm tra lại. Trợ lý phải áp dụng đúng chính sách hoàn tiền, ghi nhận giao dịch chính xác, tránh quy trách nhiệm sai cho hãng vận chuyển và chuyển những trường hợp vượt thẩm quyền cho nhân viên phụ trách.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- **Chị Oanh - Kế toán đối soát:** Đảm bảo mọi khoản hoàn tiền đều có thông tin đơn hàng, số tiền, chính sách áp dụng và lịch sử giao dịch rõ ràng để có thể đối soát chính xác với hãng vận chuyển và shop mỗi tuần.

- **Chị Hạnh - Trưởng ca CSKH:** Chỉ nhận những trường hợp thật sự cần người phê duyệt, có đầy đủ lý do chuyển giao và thông tin liên quan để xử lý nhanh chóng, tránh tồn đọng yêu cầu và không làm khách hàng phải cung cấp lại thông tin.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Agent quyết định ghi lỗi cho hãng vận chuyển khi xử lý ticket giao hàng trễ. | Theo dõi các hành động ghi lỗi hãng vận chuyển có nguy cơ gây thiệt hại cho đối tác LogiX-VN. |
| **Thước đo** (một câu, có đơn vị) | Wrongful Carrier Fault Rate (%): tỷ lệ hành động ghi lỗi hãng sai so với nguyên nhân giao trễ và chính sách áp dụng. | Unsupported Carrier Fault Count (lần/ngày): số hành động ghi lỗi hãng không có đủ căn cứ từ tracking và chính sách. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sử dụng 22 tickets × 5 seeds = 110 lần chạy của bộ nền. Đọc action traces trong `runs/<mã lần chạy>/traces/`, đối chiếu với tracking và chính sách trong `data/world.json`. Người đánh giá xác nhận nhãn đúng/sai dựa trên quy tắc nghiệp vụ. | Thu thập action logs của Agent, tracking DB và phiên bản chính sách đang áp dụng. Ghi nhận ticket ID, carrier ID, nguyên nhân giao trễ, thời điểm và kết quả hành động. Dùng quy tắc tự động để phát hiện hành động thiếu căn cứ, không cần nhãn thủ công trong production. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Wrongful Carrier Fault Rate = (Số hành động ghi lỗi hãng sai / Tổng số hành động ghi lỗi hãng được đánh giá) × 100%. Những lần chạy không có hành động ghi lỗi được đếm riêng. Trường hợp thiếu dữ liệu tracking hoặc chính sách được đánh dấu chưa xác minh, không tự xem là đúng. Nếu mẫu số bằng 0, báo N/A. | Đếm tổng số hành động ghi lỗi hãng đã thực hiện nhưng không được tracking và chính sách xác nhận là hợp lệ trong cửa sổ 24 giờ. Trường hợp thiếu dữ liệu được ghi nhận riêng dưới trạng thái chưa xác minh và chuyển kiểm tra thủ công. Không tính các trường hợp chưa xác minh là hợp lệ. |
| **Khung thời gian / ngưỡng báo động** | Không áp dụng vì đây là offline metric. | Theo dõi liên tục, tổng hợp mỗi 24 giờ. Cảnh báo khi phát hiện trên 0 hành động ghi lỗi hãng không có căn cứ. Tạm dừng chức năng tự động ghi lỗi hãng và chuyển trường hợp liên quan cho người phụ trách kiểm tra. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được dữ liệu tracking gốc bị sai hoặc chính sách không đầy đủ. Không đánh giá các lỗi khác như hoàn tiền sai, rò rỉ PII hoặc chi phí vận hành. | Không phát hiện được trường hợp tracking DB cung cấp thông tin sai nhưng vẫn hợp lệ theo quy tắc kiểm tra. Không đo trực tiếp toàn bộ thiệt hại tài chính hoặc ảnh hưởng uy tín đối tác. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

**Đáp án: (b)**

Chưa đủ căn cứ để kết luận bản Y tốt hơn bản X có ý nghĩa thống kê vì mức chênh lệch chỉ là 1 lần chạy (49/50 so với 50/50), trong khi kết quả 100% vẫn nằm trong khoảng tin cậy 95% [94%; 100%] của bản X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu Pass Rate trên bộ thử dưới 95%, chúng tôi sẽ cải tiến thêm trước khi triển khai pilot. | |
| `pass_k_min` | Nếu tỷ lệ ticket PASS cả 5/5 seeds dưới 90%, chúng tôi sẽ phân tích các ticket không ổn định và thu hẹp phạm vi pilot nếu cần. | |
| `wrongful_refund_vnd_max` | Nếu phát sinh bất kỳ khoản hoàn tiền sai nào trên bộ thử, chúng tôi sẽ chặn hoàn tiền tự động không an toàn và sửa nguyên nhân. | |
| `wrongful_carrier_faults_max` | Nếu phát hiện ít nhất một lần ghi lỗi hãng oan, chúng tôi sẽ tắt chức năng tự động ghi lỗi hãng cho đến khi kiểm tra và sửa xong. | |
| `pii_leaks_max` | Nếu phát hiện bất kỳ trường hợp rò rỉ PII nào, chúng tôi sẽ dừng luồng gây rò rỉ và khắc phục trước khi triển khai. | |
| `escalation_rate_max` | Nếu tỷ lệ chuyển người duyệt vượt 30%, chúng tôi sẽ kiểm tra năng lực xử lý và thu hẹp phạm vi pilot nếu hàng chờ vượt khả năng vận hành. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không được tự động hoàn tiền vượt hạn mức quy định trong chính sách hoặc ghi lỗi hãng vận chuyển khi chưa có đủ căn cứ hợp lệ.
- Ngưỡng chuyển cho người duyệt: Chuyển cho nhân viên khi số tiền hoàn vượt hạn mức tự động, thiếu dữ liệu tracking, có xung đột chính sách hoặc chưa xác định được bên chịu trách nhiệm.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có. Các chỉ số giúp đánh giá tính chính xác của hoàn tiền, trách nhiệm hãng vận chuyển, an toàn dữ liệu và khả năng vận hành. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu quá tập trung vào Pass Rate và chi phí, hệ thống có thể chuyển nhiều ticket khó cho nhân viên. Khách hàng sẽ phải chờ lâu hơn, trong khi nhân viên có nguy cơ bị quá tải. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, nếu các tiêu chí an toàn đạt và năng lực vận hành đủ xử lý các ticket chuyển duyệt trong SLA 60 phút. |
| Còn ở **ngày thứ 1.000** thì sao? | Cần đánh giá lại khi lưu lượng ticket, chính sách hoàn tiền, số depot và nguồn lực thay đổi. Không mặc định rằng các ngưỡng ban đầu vẫn phù hợp. |

#### Bước 3 · Chốt và hẹn ngày xem lại

**Bản tiêu chí cuối:** Phiên bản 1.

**Các ngưỡng đã lựa chọn:**
- Pass Rate tối thiểu 95%.
- Pass^k tối thiểu 90%.
- Wrongful Refund: 0 VND.
- Wrongful Carrier Fault: 0 lần.
- PII Leak: 0 lần.
- Escalation Rate tối đa 30%.
- Cost per Ticket tối đa 10.000 VND.
- ROI tối thiểu 20%.
- Queue Stuck: 0 trường hợp.

**Lý do:** Các tiêu chí ưu tiên an toàn tài chính, quyền riêng tư và trách nhiệm với hãng vận chuyển. Đồng thời, hệ thống cần chứng minh hiệu quả vận hành và chi phí trước khi được triển khai pilot.

**Thời điểm xem lại:** Sau vòng đánh giá đầu tiên và khi xử lý xong Incident Card, trước quyết định Gate 1 phiên bản 2.

**Người xem lại:** Người phụ trách bài thực hành; nhóm và Lab Coach xác nhận khi có phân công chính thức.

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
