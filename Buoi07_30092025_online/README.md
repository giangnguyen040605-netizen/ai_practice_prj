# BUỔI 07: Bài toán Phân lớp (Classification) (Online)

## 📘 Giới thiệu
Trong buổi học này, chúng ta tìm hiểu và thực hành **ba mô hình phân lớp cơ bản** trong Machine Learning:
1. **Naive Bayes** – Phân loại hoa Iris  
2. **Logistic Regression** – Phân loại chữ số viết tay (MNIST)  
3. **Decision Tree** – Phân loại rượu vang

Các bài tập được thực hiện trên các tập dữ liệu có sẵn trong thư viện `scikit-learn`.

---

## 📂 Danh sách file

| Tên file | Mô tả |
|-----------|-------|
| **📂 Folder:** `ex01_iris_classification`/`Data` | Dữ liệu mẫu cho bài Iris |
| **📄 File:** `Ex1_Classification_Iris_NaiveBayes.ipynb` | Phân loại hoa Iris bằng mô hình Naive Bayes |
| **📄 File:** `Ex2_Classification_MNIST_LogisticRegression.ipynb` | Phân loại chữ số viết tay MNIST bằng Logistic Regression |
| **📄 File:** `Ex3_Classification_Wine_DecisionTree.ipynb` | Phân loại rượu vang bằng Decision Tree |

---

## 🌸 Bài 1 – Iris Classification (Naive Bayes)

- **Mô tả**: Phân loại 3 loại hoa *Setosa*, *Versicolor*, *Virginica* dựa trên 4 đặc trưng (chiều dài/rộng đài hoa và cánh hoa).  
- **Mô hình**: `GaussianNB()`  
- **Độ chính xác**:  
  - Training accuracy: **97%**  
  - Testing accuracy: **93%**
- **Trực quan hóa**: Giảm chiều bằng PCA và vẽ scatter plot thể hiện ranh giới giữa 3 lớp hoa.

---

## 🔢 Bài 2 – MNIST Classification (Logistic Regression)

- **Mô tả**: Phân loại 10 chữ số (0–9) từ tập dữ liệu chữ số viết tay MNIST (phiên bản 8x8).  
- **Mô hình**: `LogisticRegression()`  
- **Độ chính xác**: ~**91%** trên tập kiểm tra.  
- **Đánh giá**:  
  - Sử dụng `classification_report` và `ConfusionMatrixDisplay`.  
  - Hiển thị một số hình ảnh mẫu và dự đoán tương ứng.  
- **Trực quan hóa**: PCA 2D giúp biểu diễn dữ liệu chữ số dưới dạng mặt phẳng dễ quan sát.

---

## 🍷 Bài 3 – Wine Classification (Decision Tree)

- **Mô tả**: Phân loại 3 loại rượu vang dựa trên 13 đặc trưng hóa học.  
- **Mô hình**: `DecisionTreeClassifier(max_depth=4)`  
- **Độ chính xác**: **96%** trên tập kiểm tra.  
- **Trực quan hóa**:
  - Cây quyết định bằng `plot_tree()`
  - Ma trận nhầm lẫn (Confusion Matrix)
  - Decision boundary giữa các cặp đặc trưng.

---

## Kết luận

Ba bài tập trên giúp hiểu rõ các khái niệm cơ bản trong bài toán **phân lớp (classification)**:
- Cách xử lý dữ liệu huấn luyện & kiểm thử.  
- Cách huấn luyện mô hình phân lớp khác nhau.  
- Đánh giá hiệu năng bằng **accuracy**, **F1-score**, và **Confusion Matrix**.  
- Trực quan hóa kết quả bằng PCA và biểu đồ cây.

---

👩‍💻 **Người thực hiện:** Nguyễn Khoa Châu Giang  
📧 **Email:** giangnguyen.040605@gmail.com  
📅 **Buổi 07 – Bài toán Phân lớp (Classification) (Online)**


