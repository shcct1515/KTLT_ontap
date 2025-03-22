import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv(r"C:\Users\Shcct\Desktop\KTLT_ontap\matplotlib\pokemon.csv") #nếu đưa file vào dưới dạng đường dẫn nhớ thêm r vào

# Đếm số lượng mỗi hệ Pokemon
type_counts = df['type1'].value_counts() #lấy giá trị ở cột type1 để vẽ

# Vẽ biểu đồ Bar
plt.bar(type_counts.index, type_counts.values)
plt.xlabel("Hệ Pokemon")
plt.ylabel("Số lượng")
plt.title("Số lượng Pokemon theo hệ")
plt.xticks(rotation=45)
plt.show()
