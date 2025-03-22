import pandas as pd

# Đọc file CSV
def read_csv(file_path):
    df = pd.read_csv("pokemon.csv")  # Đọc file CSV vào DataFrame LƯU Ý: nhớ thay "pokemon.csv" thành đường dẫn tới file cần đọc
    return df

# Ghi DataFrame ra file CSV
def write_csv(df, file_path):
    df.to_csv(file_path, index=False)  # Ghi DataFrame ra CSV mà không lưu index

# Hiển thị thông tin DataFrame
def dataframe_info(df):
    df.info()  # Thông tin tổng quát
    df.describe()  # Thống kê dữ liệu

# Xử lý giá trị thiếu trong CSV
def handle_missing_csv(df):
    df.fillna(0, inplace=True)  # Điền giá trị thiếu bằng 0
    df.dropna(inplace=True)  # Xóa hàng chứa giá trị thiếu

# Lọc dữ liệu từ CSV
def filter_csv_data(df, column, value):
    return df[df[column] == value]  # Lọc hàng theo điều kiện

# Thêm cột vào CSV
def add_column_csv(df, column_name, values):
    df[column_name] = values  # Thêm cột mới vào DataFrame

# Xóa cột khỏi CSV
def drop_column_csv(df, column_name):
    df.drop(columns=[column_name], inplace=True)  # Xóa cột trong DataFrame

# Sắp xếp dữ liệu từ CSV
def sort_csv_data(df, column):
    return df.sort_values(by=column)  # Sắp xếp theo cột nhất định

# Đọc file pokemon.csv và hiển thị 5 dòng đầu tiên
def load_pokemon_data():
    df = pd.read_csv("pokemon.csv")
    return df.head()

# Lọc Pokémon theo loại nhất định
def filter_pokemon_by_type(df, pokemon_type):
    return df[df['Type 1'] == pokemon_type]

# Tìm Pokémon có chỉ số tấn công cao nhất
def strongest_pokemon(df):
    return df[df['Attack'] == df['Attack'].max()]
