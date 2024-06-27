import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('./dataset/train_1.csv')
print(data.head())

data = data.head(3)

# Chuyển đổi dữ liệu từ wide sang long
data_long = pd.melt(data, id_vars=['Page'], var_name='Date', value_name='Views')

# Chuyển đổi cột Date sang định dạng datetime
data_long['Date'] = pd.to_datetime(data_long['Date'])

# Vẽ biểu đồ time series sử dụng matplotlib
plt.figure(figsize=(14, 8))

# Vẽ dữ liệu
for page in data_long['Page'].unique():
    subset = data_long[data_long['Page'] == page]
    plt.plot(subset['Date'], subset['Views'], marker='o', label=page)

# Thêm tiêu đề và nhãn
plt.title('Page Views Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Views', fontsize=14)
plt.legend(loc='upper right')

# Hiển thị biểu đồ
plt.show()
