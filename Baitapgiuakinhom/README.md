# Bài Tập Thực Hành Giữa Kỳ – Nhóm 3

## 📘 Lab 1 – Thống kê mô tả & Trực quan hóa dữ liệu
**File:** `Lab1_Ruouvangdo.ipynb`  
**Dữ liệu:** `winequality-red.csv`  
**Nguồn:** [Red Wine Quality Dataset](https://www.kaggle.com/code/eisgandar/red-wine-quality-eda-classification)

### Mục tiêu
- Thực hiện **thống kê mô tả** và **trực quan hóa** dữ liệu rượu vang đỏ.  
- Làm quen với thư viện **Pandas, Seaborn, Matplotlib, Plotly**.

### Nội dung chính
#### 🔹 Thực hiện thống kê mô tả trên tập dữ liệu về phân loại chất lượng rượu đỏ. 
#### 🔹 Thực hiện trực quan hóa dữ liệu trên tập dữ liệu về phân loại chất lượng rượu đỏ. 
- Đọc dữ liệu và kiểm tra thông tin (`df.info()`).
- Thống kê mô tả bằng `df.describe()`.
- Đổi tên cột, xử lý dữ liệu cơ bản.
- Trực quan hóa phân phối các biến (`sns.histplot`, `plt.subplots`).

---

## 📘 Lab 2 – Giải thuật Bayes Ngây thơ (Naïve Bayes)

### Bài tập Thực hành 1  
**File:** `Lab2_Naïvengaytho_BTTH1.ipynb`  
**Dữ liệu:** `Customer_Behaviour.csv`  
**Nguồn:** [Customer Behaviour Prediction](https://www.kaggle.com/code/arezalo/customer-behaviour-prediction-naive-bayes)

#### 🔹 Nội dung
- Mã hóa cột `Gender` bằng `LabelEncoder`.
- Tách dữ liệu train/test (80/20).
- Huấn luyện mô hình **GaussianNB**.
- Đánh giá mô hình với `accuracy_score`, `confusion_matrix`, `classification_report`.

#### Kết quả
- **Accuracy:** 0.94  
- Mô hình dự đoán tốt, cân bằng giữa precision và recall.

---

### Bài tập Thực hành 2  
**File:** `Lab2_Naïvengaytho_BTTH2.ipynb`  
**Dữ liệu:** `mushrooms.csv`  
**Nguồn:** [Mushroom Classification Dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification/data)

#### 🔹 Nội dung
- Mã hóa toàn bộ dữ liệu bằng `LabelEncoder`.
- Chia dữ liệu train/test (70/30).
- Huấn luyện mô hình **MultinomialNB** (phù hợp dữ liệu rời rạc).
- Đánh giá mô hình với `accuracy_score`, `confusion_matrix`, `classification_report`.

#### Kết quả
- **Accuracy:** 0.80  
- Mô hình đạt hiệu suất khá, có thể cải thiện qua tuning và chọn đặc trưng.

---

### Công cụ sử dụng
- **Ngôn ngữ:** Python  
- **Thư viện:** pandas, numpy, matplotlib, seaborn, scikit-learn  
- **Môi trường:** Google Colab / Jupyter Notebook

---

**📅 Hoàn thành:** Giữa kỳ – Môn *Kỹ thuật lập trình Stata và Python*  
**👩‍💻 Người thực hiện:** Nguyễn Khoa Châu Giang  
**👥 Bài hoàn chỉnh - Nhóm 3 thực hiện:** [Github nhóm 3](https://github.com/thylin05/NHOM_3)

