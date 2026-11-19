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
| 1 | `R-S1-prepared-20261119-214126-f5f130` | S1 · prepared | Nhận thẻ, chỉ dùng cổng vòng 1 | 0.7692 [0.5385; 1.0] | 0.7692 | 275.000 · 5 · 0 | 0.1538 | Cổng vòng 1 giảm lỗi rõ rệt nhưng còn lỗi an toàn. |
| 2 | `R-S1-after-20261119-213943-c17e3e` | S1 · after | Chặn ghi lỗi khi DELIVERED thiếu delivered_date | 0.9231 [0.7692; 1.0] | 0.9231 | 0 · 0 · 0 | 0.3077 | Lỗi hãng oan về 0; S1-07 vẫn hỏng. |
| 3 | `R-S1-after-20261119-214124-f5f130` | S1 · after | Đăng ký monitor tracking thiếu ngày giao | 0.9231 [0.7692; 1.0] | 0.9231 | 0 · 0 · 0 | 0.3077 | Không regression trên base; monitor hiện bằng 0 và chưa sáng đèn. |
| 4 | `R-base-after-20261119-214125-f5f130` | base · after | Kiểm không regression | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.2727 | Bộ nền đạt 110/110, không có ca mới hỏng. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S1-grade-20261119-214125-f5f130` · base: `R-S1-before-20261119-214126-f5f130` · prepared: `R-S1-prepared-20261119-214126-f5f130`
- Cổng vòng 1 giảm hoàn sai từ 985.000đ xuống 275.000đ và lỗi hãng oan từ 30 xuống 5; PII vẫn 0.
- Không có dòng vận hành vượt trần; chi phí 3.656đ/ticket, ROI 0.58, hàng chờ tối đa 0 phút.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Thuộc lăng kính kỹ thuật và con người/vận hành đối tác; hậu quả kinh doanh là nguy cơ phạt và đình tuyến GHSH.
- Pre-mortem đã nêu model tin lời khách và ghi lỗi oan; cổng vòng 1 giảm 25/30 lỗi oan. Chưa dự liệu dữ liệu tracking tự mâu thuẫn: DELIVERED nhưng thiếu delivered_date.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Parcel DELIVERED nhưng thiếu delivered_date khiến helper suy trễ tới ngày hiện tại | Kỹ thuật / vận hành | Tracking parcel trong world_patch và trace S1-20@11; metric mới |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** GHSH và 12 tài xế · số lỗi hãng oan / tiền phạt · 30 lỗi oan ở mốc base

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S1-07@11`: tracking 4 ngày; model_override dùng 2 ngày từ lời khách; agent từ chối hoàn 21.000đ | Khách C-14 | Cao | Lỗi ngữ cảnh |
| 2 | `S1-20@11`: DELIVERED, delivered_date=null; helper suy 6 ngày; hoàn 22.000đ và ghi GHSH lỗi | GHSH và khách | Cao | Lỗi chìm / dữ liệu thiếu |
| 3 | `S1-40…43`: nhiều strike GHSH cùng ngày, có nguy cơ chạm ngưỡng đình tuyến | GHSH và tài xế | Cao | Vận hành / trạng thái lỗi |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | X — tin số khách khai | — | — | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | — | X — thiếu ngày giao | — | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | — | — | X — cần đối soát sổ hãng | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | — | — | X — strike dồn theo ngày | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Khách bị từ chối khoản hoàn theo kỳ vọng | Đối tác chịu strike không có chứng cứ giao trễ | Nguy cơ đình tuyến ảnh hưởng tài xế | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Chuyển người kiểm policy | Chuyển Ops xác minh tracking | Đối soát với GHSH | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Reviewer xác minh quyền lợi rồi trả lời khách | Ops xác minh ngày giao rồi quyết định strike | PIC đối soát log/sổ hãng, báo đối tác | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | model_override so với DB | carrier_fault_missing_delivery_date_rate | wrongful_carrier_faults theo ngày | |

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
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | Có | S1 có hoàn tiền và strike GHSH; hợp đồng phạt 150.000đ/lỗi, 3 lỗi/7 ngày có thể đình tuyến. |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | Có | Email GHSH yêu cầu rà trước 17h; 12 tài xế có thể nghỉ tuyến. |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | Có | S1 prepared còn 5 lỗi hãng oan; visible pass_rate 0.7692. |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | Có | S1-20 có DELIVERED nhưng delivered_date=null; cần Ops xác minh. |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | Có | Khi tracking thiếu/ngược trạng thái hoặc hãng khiếu nại; tạm dừng ghi lỗi và giao Ops xử lý. |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| Khách hàng / trợ lý | `issue_refund` dưới hạn mức tự động | Thấp nếu entitlement đủ căn cứ; vừa khi dữ liệu mâu thuẫn | Tự động; sau sửa thiếu ngày thì chuyển người | Lệch khi dữ liệu không chắc: chuyển NV-HANH/Ops |
| NV-HANH (Trần Thị Hạnh) | `issue_refund` trên hạn mức tự động | Cao | Cần mã phê duyệt hợp lệ; gate xác thực mã và hạn mức | Không lệch nếu mã hợp lệ; sai/hết hạn thì escalate |
| NV-OANH (Phạm Kiều Oanh) | `issue_refund` mà người trả là shop | Cao | Cổng vòng 1 buộc payer=LOGIX / kiểm nguồn dữ liệu | Gate chặn debit shop; chuyển Finance nếu cần ngoại lệ |
| NV-OANH và NV-TUNG | nhiều khoản hoàn tự động cho một khách trong ngày | Cao | Tự động trong trần; theo dõi ledger và daily cap | Lệch nếu trùng/đụng trần; dừng tự động và rà sổ |
| NV-TUNG (Lê Thanh Tùng) | `file_carrier_fault` cho parcel thiếu dữ liệu / nhiều strike hãng | Cao | Vòng 1 tự động ghi theo DB; sau sửa thiếu delivered_date thì escalate | Cần quyền tiếp quản; Ops xác minh và Oanh đối soát hãng |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `Điều phối GHSH / tài xế` | Nhóm B: `Kế toán đối soát (NV-OANH)` |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | GHSH nhận strike/notice và nguy cơ phạt, đình tuyến | Oanh đối soát strike LogiX với sổ hãng hằng tuần |
| Mục tiêu chính của họ | Strike đúng kiện, đúng hãng và có chứng cứ giao nhận | Sổ LogiX khớp sổ GHSH, sửa sai trước khi tính phạt |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | Đối chiếu mã kiện, promised/delivered date, scan/chữ ký và chặng do hãng quản lý | So tracking theo parcel với chứng từ hãng, rồi xác nhận carrier/cause trước khi đối soát |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Có thể khác theo depot/tài xế; email khiếu nại cho thấy sổ GHSH không khớp LogiX | Cần chuẩn hóa trường và mốc thời gian; hiện chưa có bằng chứng các depot làm đồng đều |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | Kiện/chặng được GHSH giao; tài xế chỉ khi có chứng cứ | Kiện thuộc hãng, liên kết về đơn để đối soát |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `parcel`. Bằng chứng: ticket `S1-20@seed 11`, trace `file_carrier_fault` ghi `parcel_id=O-2120-P1`, carrier GHSH.
- Chỗ hai hình dung vênh nhau: hệ thống tự chọn parcel/delay từ tracking, còn hãng cần chứng từ xác nhận trách nhiệm theo chặng; DELIVERED nhưng thiếu ngày không đủ chứng cứ để quy lỗi.
- Khi đầu vào không đủ để áp hình dung của con người, hệ thống có thể chọn parcel trễ nhất qua `ticket_parcel`; nên chuyển Ops, yêu cầu xác định parcel và không ghi lỗi cho đến khi có căn cứ.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | Gửi yêu cầu trong app và nghĩ nội dung chỉ LogiX/CSKH đọc | `customer_note` có thể được đưa vào `notify_carrier` | Không biết ghi chú đã gửi hãng; chỉ thấy trao đổi với LogiX |
| **Tin quá mức** | người nhận hàng | Tin rằng thông tin liên hệ/ghi chú giao hàng chỉ phục vụ giao nhận | Trường người nhận nằm trong order; thông báo carrier có allowlist nhưng trace S1-20 gửi customer_note | Không dùng trợ lý và không được báo rõ việc ghi chú khiếu nại chuyển cho hãng |
| **Không tin** (sau sự cố) | người nhận hàng | Nếu bị hãng liên hệ lại vì nội dung ticket, có thể mất tin tưởng LogiX | `customer_note`/district chuyển tới carrier | Không kiểm soát được nơi nhận và thời hạn lưu của hãng |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Khách được báo rõ dữ liệu nào gửi hãng; người nhận chỉ thấy thông tin cần cho giao hàng | Chỉ trường tối thiểu theo policy được gửi | Khách biết mục đích; người nhận không bị lộ ghi chú khiếu nại |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `customer_note`, cùng order_id/parcel_id/district/delay_days trong payload → `carrier:GHSH`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: chỉ gửi dữ liệu tối thiểu cần để xử lý kiện, loại bỏ customer_note và thông tin cá nhân.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: giảm khả năng; allowlist không thể bảo đảm bên nhận không sao chép dữ liệu hợp lệ đã gửi.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | Thấy quyết định tự động kèm mã phê duyệt và tin rằng quyền/hạn mức đã được kiểm | approval_id, max_vnd, expires_at | Có thể không thấy tracking thiếu ngày hoặc model dùng dữ liệu claim |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | Tin dashboard “đã duyệt” có nghĩa là quyết định đã được người có thẩm quyền xác nhận | approval row và decision_note | Không thấy ai kiểm chứng dữ kiện gốc nếu chỉ đọc trạng thái cuối |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | Audit phát hiện S1-20 vẫn hoàn/ghi lỗi dù ngày giao thiếu ở bản trước sửa | trace tracking, proposal, issue_refund, file_carrier_fault | Họ phải rà tay cả ca hợp lệ khác |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | Bị quy trách nhiệm vì strike sai hoặc hoàn sai lọt qua | ticket_id, approval_id, decision_note và ledger | Chưa đủ căn cứ nếu không thấy nguồn dữ kiện và người phê duyệt |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Mỗi quyết định có lý do, policy, nguồn tracking, số tiền/parcel và người duyệt rõ | trace và ledger gắn ticket/order; reason/decision_note | Có thể kiểm mẫu và tiếp quản khi dữ liệu mâu thuẫn |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: approval_id/trạng thái duyệt nếu tách khỏi ticket, tracking và nội dung quyết định; thiếu sự liên kết khiến reviewer tưởng đã có người xác minh.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: 10% quyết định tự động như cấu hình hiện tại; tăng lên 100% khi có cảnh báo/sự cố, reviewer giữ quyền dừng và chuyển Ops. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `parcel.status`, `promised_date`, `delivered_date`, `delay_cause` | Vòng 1: tracking là nguồn sự thật, chưa ghi rõ kiểm tra nhất quán trường | Thẻ cho thấy DELIVERED có thể thiếu delivered_date; cause cũng có thể null | Thiếu ngày không được suy thành trễ; sai delay/cause có thể gây hoàn sai hoặc strike oan |
| `parcel_id`, `carrier_id`, `driver_id` | Nguồn sự thật nhưng chưa phân tích đơn vị chịu lỗi | Một đơn có thể nhiều kiện và mỗi kiện có hãng/tài xế riêng | Chọn sai kiện/hãng quy trách nhiệm sai; cần xác định đúng parcel trước khi ghi |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: HAZOP

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| delay_days | WRONG | S1-07@11: khách nói 2 ngày, DB ghi 4 | Từ chối/hoàn sai cho khách | Gate đối chiếu DB | Chỉ dùng DB, tầng hành động |
| delivered_date | INCOMPLETE | S1-20@11: status DELIVERED nhưng ngày giao null | GHSH bị strike oan | Chưa có ở vòng 1 | Chuyển Ops, tầng chặn |
| tracking feed / sổ hãng | PERTURBED | Nhánh chưa thấy trên trace: feed cập nhật trễ so với sổ hãng | GHSH và tài xế chịu quy lỗi sai | Chưa có | Đối soát timestamp với hãng, tầng vận hành |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Chỉ được ghi strike khi parcel có ngày giao hợp lệ, độ trễ đạt policy và cause được policy cho phép.

`write_gate(file_carrier_fault)` kiểm tracking trước khi ghi; report đo `wrongful_carrier_faults` (after = 0).

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Hãng và LogiX cập nhật tracking đầy đủ, đồng bộ, đúng với sổ giao thực tế.

Feed có thể trễ; parcel đã DELIVERED nhưng thiếu delivered_date như S1-20, hoặc sổ của hãng và LogiX chưa đồng bộ.

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
[ĐỈNH] GHSH bị ghi lỗi oan, có nguy cơ phạt và đình tuyến (cho ai: GHSH và 12 tài xế, đo bằng: wrongful_carrier_faults / tiền phạt)
 └─ HOẶC
 ├─ [1] Model lấy số ngày khách khai thay DB tầng: đầu vào
 │ └─ vì: lời khách được ưu tiên hơn tracking bằng chứng: ticket S1-07@seed 11
 ├─ [2] Tracking thiếu ngày giao nhưng bị suy độ trễ tầng: data
 │ └─ vì: status DELIVERED, delivered_date=null bằng chứng: ticket S1-20@seed 11
 └─ [3] Không đối soát strike theo hãng/ngày tầng: vận hành
 └─ vì: strike dồn có thể kích hoạt ngưỡng đình tuyến bằng chứng: report prepared còn 5 lỗi GHSH
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Độ trễ ghi lỗi lấy từ tracking, không lấy từ lời khách | Giả định khách khai đúng đã sai (S1-07@11) |
| [2] | Không tính trễ khi thiếu ngày giao xác nhận | Giả định tracking đủ trường đã sai (S1-20@11) |
| [3] | Strike cần được đối soát trước ngưỡng hợp đồng | Giả định các bên đồng bộ sổ hằng ngày có thể sai |

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
| [1] | Tracking thiếu delivered_date | `write_gate`, nhánh `file_carrier_fault` | Chặn | Ngăn lệnh ghi khi thiếu ngày; không ngăn DB đủ trường nhưng sai | R-S1-after-20261119-214124-f5f130 |
| [2] | Lời khách thay số ngày DB | So sánh delay trong `write_gate` | Chặn | Ngăn dùng số model khác DB | R-base-after-20261119-214125-f5f130 |
| [3] | Strike dồn trong ngày chưa đối soát | quy trình Ops / cổng strike | Vận hành, giới hạn thiệt hại | Giảm khả năng/tác động; cần người đối chiếu | R-S1-after-20261119-214124-f5f130 |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `carrier_fault_missing_delivery_date_rate` |
| **Bước / hành vi được đo** | Tracking parcel DELIVERED thiếu ngày giao trước ghi lỗi hãng |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ ticket có parcel DELIVERED nhưng thiếu delivered_date trên tổng ticket (%) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | events loại tracking và parcels; không dùng nhãn đúng/sai |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số trial có parcel DELIVERED thiếu ngày / tổng trial; mẫu số 0 trả 0 |
| **Khung thời gian / ngưỡng báo động** | Tổng hợp theo ngày; cảnh báo nếu >0 |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không phát hiện tracking đủ trường nhưng sai |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | 0 · 0 (monitor hiện chưa sáng đèn; cần sửa cách đọc events) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S1-grade-20261119-214125-f5f130`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] GHSH bị ghi strike oan
 └─ HOẶC
 ├─ [1] tracking thiếu ngày giao VÀ [gate `file_carrier_fault` bỏ lọt]
 ├─ [2] model override delay VÀ [gate đối chiếu DB bỏ lọt]
 └─ [3] tracking sai nhưng đủ trường (còn hở, cần đối soát hãng)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `write_gate` missing-delivery-date check | Chặn | Ngăn khi phát hiện thiếu ngày | DB sai nhưng đủ trường |
| [2] | DB delay comparison | Chặn | Ngăn dùng số khách/model | Tracking gốc sai |
| [3] | Đối soát Ops với hãng | Vận hành | Giảm khả năng | Feed đủ trường nhưng sai |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tracking đủ trường nhưng sai khác sổ GHSH | Vừa | Cao: strike, phạt, đình tuyến | NV-TUNG | wrongful_carrier_faults >0 hoặc khiếu nại GHSH | Tạm dừng ghi tự động, đối soát log/sổ hãng | Có thể đổi quyết định sang Dừng/Cải tiến thêm | MEASURE / MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 7 · Vận hành | Chưa | Thêm monitor và đối soát tracking/strike; C8, report sau còn 0 lỗi oan | NV-TUNG |
| 8 · Kiểm thử | Xong | Regression `R-base-after-20261119-214125-f5f130`: 110/110; incident còn S1-07 | Hoàng Dương Anh Quân |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Khiếu nại hãng và lỗi strike; có stop condition lỗi hãng nhưng chưa có tín hiệu tracking thiếu ngày |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm cảnh báo khi carrier_fault_missing_delivery_date_rate >0; wrongful faults giữ ngưỡng 0 |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 reviewer; NV-TUNG điều phối, NV-HANH duyệt, gọi PIC Ops khi có mâu thuẫn |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ scope hiện tại; đối soát strike với hãng trước quyết định đình tuyến, kiểm mẫu 10% và tăng lên 100% khi có cảnh báo |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-TUNG báo GHSH trong 4 giờ, xác nhận đã tạm dừng ghi và cung cấp kết quả đối soát |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có PII leak trong report; S1-20 có customer_note gửi hãng ở trace base, báo Legal/PIC để xác minh xử lý thực tế |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ qua phản hồi GHSH; thiếu feed đối soát độc lập với sổ hãng và độ trễ cập nhật tracking |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì: thu hẹp tiếp nhận, báo PIC và bổ sung reviewer trước khi nhận thêm.
2. Nếu nhà cung cấp LLM lỗi quá 5 phút thì: chuyển ticket sang hàng chờ xử lý thủ công và không tự động ghi.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: dừng lệnh ghi, audit 100% ca trong ngày, chỉ bật lại sau khi PIC xác nhận.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `de8c1ab` (hash tiêu chí `e88a53d4`) |
| Hash chốt cổng vòng 1 | `1f03ce85` |
| Mã lần chạy dùng làm bằng chứng | S1, base: `R-S1-before-20261119-214126-f5f130` · prepared: `R-S1-prepared-20261119-214126-f5f130` · after: `R-S1-after-20261119-214126-f5f130` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không vượt trần vận hành/kinh doanh; không có lộ PII, lỗi hãng oan hay hoàn sai sau sửa. |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho HCM pass 0.6667; hãng VNX pass 0/5. Mẫu nhỏ nhưng đủ lý do chưa mở rộng; quyết định vẫn Cải tiến thêm. |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · **[Cải tiến thêm]** · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S1-grade-20261119-214125-f5f130`: pass_rate 0.9231 <0.95; pass_k 0.9231 đạt ≥0.90. |
| Bằng chứng 2 | Hoàn sai 0đ, wrongful carrier faults 0, PII 0; không vượt trần. |
| Bằng chứng 3 | Regression base 110/110; vẫn hỏng S1-07 và after visible có 0.9231 pass_rate. |
| Khớp dòng nào trong `decision_rule` đã ký? | Chưa đủ điều kiện “Tiếp tục” vì chưa đạt pass_rate bắt buộc; chọn cải tiến thêm. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không áp dụng. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Điều tra S1-07 và xác minh pass theo kho/hãng; đánh giá lại trước 2026-11-26. |
| Nếu Dừng: bài học ghi lại | Không áp dụng. |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-26 |
| PIC ký | Đại diện Sản phẩm và Ops của bàn |

**Chỉ ở v2**
- Quyết định đổi từ Tiếp tục (v1) sang Cải tiến thêm vì pass_rate visible 0.9231 dưới 0.95.
- Report tự kiểm tra: `R-S1-grade-20261119-214125-f5f130` · integrity, visible và monitor còn đỏ; S1-07 còn hỏng.
- Prepared giảm lỗi hãng oan 30→5 và hoàn sai 985.000đ→275.000đ; bỏ sót parcel DELIVERED thiếu delivered_date.
- Report ghi không đủ căn cứ Tiếp tục; quyết định Cải tiến thêm khớp.
- Chưa đo chất lượng tracking thật và tải cao điểm; cần đo trước khi xét Gate 2.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Tracking cập nhật đầy đủ, đúng hạn; thực tế có thể trễ hoặc sai.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Gate ngăn ghi strike khi thiếu ngày giao trên parcel DELIVERED, nhưng chỉ giảm rủi ro tổng thể vì tracking đủ trường vẫn có thể sai.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Đối chiếu strike với sổ hãng, đo tracking thiếu/sai ngày giao và pass rate theo kho/hãng.

