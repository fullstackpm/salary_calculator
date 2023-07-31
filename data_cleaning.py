import pandas as pd

data = pd.read_csv("Salary_Data.csv").values

# detecting symbols in data
symbols = ['?', '*', '#', 'Nan', '']
for row in data:
    if set(row) & set(symbols):
        print(row)