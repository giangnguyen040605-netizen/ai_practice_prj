# Buổi 04: Phân loại Iris & Phân tích dữ liệu tài chính (09/09)

## Mục tiêu
Buổi 04 tập trung thực hành **hai nội dung chính**:
1. **Phân loại hoa Iris** bằng các kỹ thuật tiền xử lý và khám phá dữ liệu (EDA).  
2. **Phân tích dữ liệu tài chính định lượng** bằng Python (sử dụng `pandas`, `yfinance`, `mplfinance`...).

---

## Phần 1: Phân loại Iris (`iris_classification.ipynb`)

### Nội dung chính
- Nạp dữ liệu từ thư viện `sklearn` hoặc file `iris.csv`.  
- Khám phá dữ liệu: kiểm tra kích thước, kiểu dữ liệu, giá trị rỗng, thống kê mô tả.  
- Phân tích mối tương quan giữa các đặc trưng bằng **Heatmap** và **Pairplot**.  
- Trực quan hóa dữ liệu bằng **Boxplot**, **Histogram**, **Scatterplot**.  
- Nhận xét sự khác biệt giữa ba loài hoa: *Setosa*, *Versicolor*, *Virginica*.  
- Làm sạch dữ liệu (xóa dòng trùng, chuẩn hóa dữ liệu đầu vào).

### Kết quả
- Dữ liệu gồm **147 dòng** sau khi làm sạch.  
- Mối tương quan mạnh giữa `petal_length` và `petal_width`.  
- Biểu đồ cho thấy mỗi loài hoa có vùng giá trị đặc trưng rõ rệt.

---

## Phần 2: Phân tích dữ liệu tài chính (`EDA-Fin.ipynb`)

### Nội dung chính
- Tải dữ liệu cổ phiếu từ **Yahoo Finance** bằng thư viện `yfinance`.  
- Khám phá dữ liệu: giá mở cửa, đóng cửa, khối lượng giao dịch.  
- Trực quan hóa xu hướng giá bằng **Line chart** và **Candlestick chart**.  
- Phân tích hiệu suất giữa các mã cổ phiếu theo thời gian.  
- Ứng dụng `pandas` và `mplfinance` trong trực quan dữ liệu tài chính.

---

## Tổng kết
| Notebook | Chủ đề | Nội dung chính |
|-----------|---------|----------------|
| `iris_classification.ipynb` | Phân loại | EDA & trực quan hóa dữ liệu hoa Iris |
| `EDA-Fin.ipynb` | Phân tích tài chính | Truy xuất và trực quan dữ liệu đầu tư |

---

👩‍💻 **Người thực hiện:** Nguyễn Khoa Châu Giang  
📧 **Email:** giangnguyen.040605@gmail.com  
📅 **Buổi 4 – Phân loại Iris & Phân tích dữ liệu tài chính**
