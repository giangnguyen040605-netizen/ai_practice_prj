# 🌍 Bài Tập Cuối Kỳ Nhóm 3 - Phân nhóm quốc gia theo mức phát thải CO₂ (Classification)

**File Notebook:** `PhannhomCO2.ipynb`  
**File dữ liệu:** `DataCO2.xlsx`

## Mục tiêu
Phân loại các quốc gia theo mức phát thải CO₂ trong **năm 2023** (Low – Medium – High), nhằm cung cấp góc nhìn tổng quan về sự phân bố phát thải toàn cầu và làm cơ sở phân tích mối liên hệ giữa kinh tế, dân số và năng lượng.

---

## Quy trình thực hiện

### 1️⃣ Chuẩn bị dữ liệu
- Nạp dữ liệu từ `DataCO2.xlsx`, lọc riêng **năm 2023**.  
- Tạo biến mục tiêu `co2_group` gồm 3 nhóm (Low, Medium, High) theo **phân vị 33% và 66%**.  
- Loại bỏ các biến thiếu toàn bộ dữ liệu (`gdp`, `co2_per_gdp`).  
- Chuẩn hóa và xử lý missing values bằng `SimpleImputer` và `StandardScaler`.

---

### 2️⃣ Xây dựng mô hình
**Mô hình 1 – Logistic Regression**  
- Tối ưu tham số `C` và `solver` bằng `GridSearchCV`.  
- Độ chính xác ~ **0.69**, mô hình phân loại khá ổn với dữ liệu hạn chế.  

**Mô hình 2 – Decision Tree**  
- Tối ưu tham số `max_depth`.  
- Kết quả: `max_depth = 5`, độ chính xác test ~ **0.82**.  
- Trực quan hóa độ chính xác train/test theo độ sâu của cây.

**Mô hình 3 – Random Forest**  
- Dò lưới tham số `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`.  
- Mô hình tốt nhất: **Accuracy = 0.90**, CV ≈ **0.92**.  
- Các lớp đều được dự đoán tốt, đặc biệt nhóm phát thải cao (High).

---

### 3️⃣ Đánh giá mô hình
- Dùng Test Accuracy làm thước đo chính để so sánh hiệu suất tổng thể giữa các mô hình.
- Dùng F1-score cho từng nhóm (Low, Medium, High) để đánh giá độ cân bằng giữa Precision và Recall của từng lớp.
- Trực quan hóa bằng ConfusionMatrixDisplay cho từng mô hình cung cấp chi tiết dự đoán đúng/sai cho từng nhóm (Low, Medium, High).
- Random Forest thể hiện độ ổn định và độ chính xác cao nhất, đồng thời có F1-score tốt nhất ở cả ba nhóm.

---

### 4️⃣ Phân tích đặc trưng quan trọng
Top 3 biến ảnh hưởng lớn nhất đến phát thải CO₂:
1. **oil_co2** – lượng CO₂ từ dầu mỏ  
2. **gas_co2** – lượng CO₂ từ khí đốt  
3. **cement_co2** – lượng CO₂ từ sản xuất xi măng  

Trực quan hóa bằng biểu đồ **Feature Importance** (màu gradient).

---

## Kết luận
- Rừng cây ngẫu nhiên (**Random Forest**) là mô hình tối ưu để phân nhóm quốc gia theo mức phát thải CO₂.  
- Kết quả cho thấy **nguồn năng lượng hóa thạch** là yếu tố chính ảnh hưởng đến phát thải toàn cầu.

---

**📅 Hoàn thành:** Cuối kỳ – Môn *Kỹ thuật lập trình Stata và Python*  
**👩‍💻 Người thực hiện:** Nguyễn Khoa Châu Giang  
**👥 Bài hoàn chỉnh - Nhóm 3 thực hiện:** [Github nhóm 3](https://github.com/thylin05/NHOM_3)
