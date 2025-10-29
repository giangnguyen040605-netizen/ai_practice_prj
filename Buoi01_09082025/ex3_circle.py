# ex3_circle.py
# Tính chu vi và diện tích hình tròn

import math

# Nhập bán kính từ bàn phím
r = float(input("Nhập bán kính hình tròn (r): "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r**2

# In kết quả ra màn hình
print(f"Chu vi hình tròn = {cv:.2f}")
print(f"Diện tích hình tròn = {dt:.2f}")