import pandas as pd

# Tạo Series
def create_series():
    data = [10, 20, 30, 40] # dữ liệu của series
    index = ['a', 'b', 'c', 'd'] #tạo index cho series
    series = pd.Series(data, index=index)  # Tạo Series
    return series

# Tạo DataFrame
def create_dataframe():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Score': [85, 90, 95]}
    df = pd.DataFrame(data)  # Tạo DataFrame từ Dictionary
    return df

# Truy cập dữ liệu trong Series
def access_series(series):
    series['a']  # Lấy phần tử theo nhãn
    series[0]  # Lấy phần tử theo vị trí
    series[:2]  # Lấy phần tử từ đầu đến index 2

# Truy cập dữ liệu trong DataFrame
def access_dataframe(df):
    df['Name']  # Lấy cột 'Name'
    df.loc[0]  # Lấy hàng đầu tiên bằng label
    df.iloc[1]  # Lấy hàng thứ 2 bằng vị trí

# Thêm cột vào DataFrame
def add_column(df):
    df['Passed'] = df['Score'] > 80  # Thêm cột dựa trên điều kiện

# Xóa cột khỏi DataFrame
def drop_column(df):
    df.drop(columns=['Score'], inplace=True)  # Xóa cột 'Score'

# Sắp xếp DataFrame
def sort_dataframe(df):
    df.sort_values(by='Age', ascending=False)  # Sắp xếp theo tuổi giảm dần