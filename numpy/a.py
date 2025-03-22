import numpy as np

# Mảng 1 chiều
def array1d():
    arr = np.array([3, 4, 6, 8])  # Khai báo mảng 1 chiều
    arr[0]  # Lấy phần tử đầu tiên
    arr[-1]  # Lấy phần tử cuối cùng
    arr[2]  # Lấy phần tử thứ 3
    arr[1:3]  # Lấy phần tử từ index 1 đến 3

# Mảng 2 chiều
def array2d():
    arr = np.array([[2, 3, 4], [5, 6, 7]])  # Khai báo mảng 2 chiều
    arr[0, 1]  # Lấy phần tử ở hàng 0 cột 1
    arr[:, 1]  # Lấy tất cả hàng, cột 1

# Các hàm tạo mảng đặc biệt
def special_arrays():
    np.zeros((2, 3))  # Tạo mảng toàn 0
    np.ones((3, 3))  # Tạo mảng toàn 1
    np.arange(1, 10, 2)  # Tạo mảng cách đều 2 đơn vị
    np.linspace(0, 1, 5)  # Tạo mảng gồm 5 số cách đều từ 0 đến 1

# Các phép toán trên mảng
def operations():
    arr = np.array([1, 2, 3, 4])
    arr.sum()  # Tổng tất cả phần tử
    arr.mean()  # Trung bình cộng
    arr.std()  # Độ lệch chuẩn
    arr * 2  # Nhân toàn bộ mảng với 2
    arr + 10  # Cộng 10 vào tất cả phần tử

# Thay đổi hình dạng mảng
def reshape_array():
    arr = np.array([1, 2, 3, 4])
    arr.reshape(2, 2)  # Chuyển thành mảng 2x2
    arr.T  # Chuyển vị (Transpose)

# Sắp xếp mảng
def sort_array():
    arr = np.array([3, 1, 4, 2])
    np.sort(arr)  # Sắp xếp tăng dần
    np.sort(arr)[::-1]  # Sắp xếp giảm dần
