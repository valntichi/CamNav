import pandas as pd
data_xls = pd.read_excel('data/AB_location_data.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('your_csv.csv', encoding='utf-8')
