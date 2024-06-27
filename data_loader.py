import pandas as pd

def load_dataset() -> pd.DataFrame:
    # Load data
    data = pd.read_csv('./dataset/train_1.csv.zip', compression="zip")

    # Chuyển đổi dữ liệu từ wide sang long
    data_long = pd.melt(data, id_vars=['Page'], var_name='Date', value_name='Views')

    # Chuyển đổi cột Date sang định dạng datetime
    data_long['Date'] = pd.to_datetime(data_long['Date'])

    return data_long
