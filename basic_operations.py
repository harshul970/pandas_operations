import pandas as pd

str_trade_data_file_path = r"Input/Trade_Test_Data.xlsx"
df_trade_data = pd.read_excel(str_trade_data_file_path, sheet_name="MasterData")
print(df_trade_data)
