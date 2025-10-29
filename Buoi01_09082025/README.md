# Làm quen với Codespaces và Jupyter-Lab
## Phần 1: Giới thiệu

Dự án này được thực hiện nhằm làm quen với môi trường lập trình trên GitHub Codespaces kết hợp với Jupyter-Lab, giúp sinh viên nắm vững quy trình làm việc, lập trình trực quan và quản lý mã nguồn trên GitHub.
## Phần 2: Lập trình trên Jupyter-Lab
### Bài 1 – ex1_scientific1.ipynb

Mục tiêu: Hiển thị ngẫu nhiên 50 hình tròn trên mặt phẳng.

Nội dung chính:
Sinh ngẫu nhiên tâm $(x_i, y_i)$, màu sắc và bán kính $r_i$.
Tính diện tích $area_i = \pi r_i^2$.
Hiển thị đồ thị bằng matplotlib.pyplot.

Kết quả đạt được:
Chạy thành công notebook trên Codespaces.
Biểu đồ scatter hiển thị 50 hình tròn với kích thước, vị trí và màu sắc ngẫu nhiên.

Thư viện sử dụng:
import numpy as np
import matplotlib.pyplot as plt
from IPython import display

### Bài 2 – ex2_scientific2.ipynb

Mục tiêu: Hiển thị 2 đồ thị hàm số sin(x) và cos(x) trong khoảng $[-\pi, \pi]$.

Các bước thực hiện:
Sinh dữ liệu X = np.linspace(-np.pi, np.pi, 256).
Tính C = np.cos(X) và S = np.sin(X).
Vẽ đồ thị hai hàm số trên cùng một trục tọa độ với màu và định dạng khác nhau.

Kết quả đạt được:
Hai đường cong sin và cos được hiển thị rõ ràng trên cùng một đồ thị.
Trục tọa độ được tùy chỉnh với nhãn $-\pi$, $-\pi/2$, $0$, $+\pi/2$, $+\pi$.

Thư viện sử dụng:
import numpy as np
import matplotlib.pyplot as plt
