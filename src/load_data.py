import pandas as pd
import json
import polars as pl
### loading csv file
df_csv = pd.read_csv(r'.\data\raw\student_coffee_crisis.csv')

print("\n ######The first five rows of the csv file:#######\n",df_csv.head())
#pd.read_csv('data.csv',sep=';',encoding='utf-8',skiprows=1)

### loading json file
df_json = pd.read_json(r'data\raw\student_coffee_crisis.json')
print("\n ######The first five rows of the json file:#######\n",df_json.head())
# nested JSON → use json + normalize
#data = json.load(open('data.json'))
#df = pd.json_normalize(data)

### loading excel file
df_xls = pd.read_excel(r'data\raw\student_coffee_crisis.xlsx')
print("\n ######The first five rows of the excel file:#######\n",df_xls.head())
# specific sheet:
#df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

### loading parquet file
# Load into memory immediately
df_par = pl.read_parquet(r'data\raw\student_coffee_crisis.parquet')
print("\n ######The first five rows of the parquet file:#######\n",df_par.head())
# Or scan it (Lazy evaluation - processes data only when needed)
#lazy_df = pl.scan_parquet('data.parquet').select(['user_id', 'age']).collect()