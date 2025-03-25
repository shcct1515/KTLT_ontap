""" câu 1 """

import pandas

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

print(df.head(10))

"""câu 2 demo"""

import pandas

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")
#shape[0] là hàng, shape[1] là cột
print(df.shape[0], df.shape[1])
#in danh sách các cột
print(df.columns)

"""câu 3 demo"""

import pandas

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

dffil = df[(df["base_total"] >= 600) & (df["generation"] == 6)]

print(dffil[["name", "base_total", "type1"]])

"""câu 4"""

import pandas

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

data = df.groupby("type1")["defense"].mean().sort_values(ascending = False)

print(data)

"""câu 5"""

import pandas

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

is_legendary = df[df["is_legendary"] == 1].shape[0]
isnt_legendary = df[df["is_legendary"] == 0].shape[0]
#is_legendary = df["is_legendary"].value_counts()

print(is_legendary, isnt_legendary)

"""câu 6"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

data = df['generation']
print(data.value_counts())
plt.bar(data.value_counts().index, data.value_counts())
plt.xlabel("thế hệ")
plt.ylabel("số lượng")
plt.title("số lượng pokemon theo thế hệ")
plt.show()

"""câu 7"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

data = df[df["type2"].notna()]
print(data["type2"].value_counts())
plt.pie(data["type2"].value_counts(), labels = data["type2"].value_counts().index, autopct = "%1.1f%%", pctdistance=0.8)
plt.title("số lượng pokemon theo type2")
plt.legend(bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()

"""câu 8"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

data = df[df["speed"] >= 120]
print(data[["name", "generation"]])

"""câu 9"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

is_legendary = df[df["is_legendary"] == 1]["generation"].value_counts()
print(is_legendary)
plt.bar(is_legendary.index, is_legendary)
plt.title("số lượng pokemone huyền thoại theo thế hệ")
plt.xlabel("số lượng")
plt.ylabel("thế hệ")
plt.show()

"""câu 10"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv(r"/content/sample_data/pokemon.csv")

data = df[df["percentage_male"] > 50].shape[0]
data2 = df[df["percentage_male"] <= 50].shape[0]
data3 = df["percentage_male"].isna().sum()

print("Lớn hơn 50%:", data)
print("Nhỏ hơn hoặc bằng 50%:", data2)
print("Không xác định:", data3)

labels = ["lớn hơn 50%", "nhỏ hơn 50%", "không xác định"]
sizes = [data, data2, data3]

plt.pie(sizes, labels = labels, autopct="%.1f%%")
plt.title("số lượng pokemon theo giới tính nam")
plt.show()
