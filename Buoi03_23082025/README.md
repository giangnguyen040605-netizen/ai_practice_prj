# BUỔI 3: Phân tích và hiển thị dữ liệu với Python (23/08)
## Thực hành Exploratory Data Analysis (EDA) trong Python
## Mục tiêu  
Nắm vững các bước **phân tích dữ liệu khám phá (EDA)** bằng Python thông qua bộ dữ liệu **Iris** kinh điển, sử dụng các thư viện phổ biến như `pandas`, `matplotlib`, `seaborn` và `numpy`.  

---

## Nội dung chính  

### 1. Giới thiệu và nạp dữ liệu  
- Sử dụng bộ dữ liệu `iris` từ thư viện `seaborn` hoặc `sklearn`.  
- Xem nhanh cấu trúc dữ liệu, kiểu dữ liệu và giá trị bị thiếu.  

### 2. Phân tích không trực quan (Non-Graphical EDA)  
- Kiểm tra kích thước dữ liệu, thông tin cột, kiểu dữ liệu và mô tả thống kê (`df.describe()`).  
- Kiểm tra phân bố các lớp (`species`) để xem dữ liệu có cân bằng hay không.  

### 3. Phân tích tương quan giữa các biến  
- Tính ma trận tương quan để đánh giá mối liên hệ giữa các thuộc tính định lượng như `sepal_length`, `petal_width`...  

### 4. Phân tích trực quan (Graphical EDA)  
- **Biểu đồ tần suất (Bar plot, Count plot)**: Quan sát sự cân bằng giữa các lớp loài hoa.  
- **Biểu đồ phân tán (Scatter plot)**: Thể hiện mối quan hệ giữa các cặp biến.  
- **Biểu đồ ma trận (Pairplot/Correlogram)**: Khám phá xu hướng và phân tách giữa các loài.  
- **Heatmap**: Trực quan hóa ma trận tương quan giữa các biến số.  
- **Histogram và Boxplot/Violin plot**: Thể hiện phân phối và so sánh giá trị giữa các loài hoa.  

---

## 📊 Kết quả đạt được  
- Hiểu được cấu trúc và đặc điểm của bộ dữ liệu Iris.  
- Nhận biết rõ mối tương quan mạnh giữa `petal_length` và `petal_width`.  
- Thực hành thành thạo các biểu đồ cơ bản phục vụ bước phân tích dữ liệu ban đầu trong Machine Learning.  

---

## 📁 File trong thư mục [BT] 03 - EDA-Python
- `ThuchanhBT(EDA-Python).ipynb`: Notebook chính chứa toàn bộ quy trình phân tích.  

