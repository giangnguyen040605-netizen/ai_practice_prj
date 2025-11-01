# BUỔI 06 – Tiền xử lý dữ liệu & Mô hình (Online)

## Mục tiêu  
Thực hành các kỹ thuật **tiền xử lý dữ liệu (data preprocessing)** và **biến đổi đặc trưng (feature transformation)** trong Python, đồng thời xử lý dữ liệu thiếu và đánh giá hiệu quả mô hình sau khi biến đổi.  

---

## Nội dung chính  
### 1️⃣ Feature Engineering 
**📄 File:** `ex1_FeatureEngineering.ipynb`  
- Sử dụng `StandardScaler`, `PCA`, `ICA`, và `SymbolicTransformer` (GP) để biến đổi dữ liệu.  
- Thực hiện quy trình **fit trên tập train**, **transform trên tập test**.  
- Huấn luyện và so sánh mô hình `RandomForestClassifier` / `LogisticRegression` trước và sau biến đổi.  

**Kết quả mẫu:**  
| Phương pháp | Accuracy |
|--------------|-----------|
| Dữ liệu gốc | 0.91 |
| PCA | 0.93 |
| ICA | 0.93 |
| GP Transformer | **0.98** |

---

### 2️⃣ Xử lý dữ liệu thiếu
**📄 File:** `ex2_MissingValues.ipynb`  
- Dữ liệu: **Titanic (OpenML)**  
- Các bước thực hiện:  
  - Phát hiện giá trị khuyết (`NaN`, `?`).  
  - Xóa cột hoặc hàng có dữ liệu thiếu.  
  - Bổ khuyết dữ liệu bằng:
    - `SimpleImputer` (mean/median/mode)  
    - `KNNImputer`  
    - `IterativeImputer`  
  - Mã hóa biến phân loại bằng `OrdinalEncoder` (`sex`, `cabin`).  

---

### 3️⃣ Trực quan hóa 
**📄 File:** `ex3_eg_plot_3_features.ipynb`  
- Trực quan hóa dữ liệu **Iris** qua biểu đồ 3D hoặc `pairplot` để quan sát phân tách giữa các lớp.  

---

## Công cụ sử dụng  
- **Jupyter lab**  
- **Python libraries:**  
  `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `gplearn`, `seaborn`  

---

## Kết quả đạt được  
- Hiểu quy trình **fit–transform** trong `sklearn`.  
- Thực hành chuẩn hóa, giảm chiều, và xử lý giá trị thiếu.  
- Quan sát ảnh hưởng của **feature transformation** đến hiệu suất mô hình.  
- Củng cố kỹ năng **tiền xử lý và trực quan hóa dữ liệu** trong pipeline phân tích.
  
---

👩‍💻 **Người thực hiện:** Nguyễn Khoa Châu Giang  
📧 **Email:** giangnguyen.040605@gmail.com  
📅 **Buổi 06 – Tiền xử lý dữ liệu & Mô hình**
