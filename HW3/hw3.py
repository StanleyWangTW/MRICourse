import pandas as pd

df = pd.read_excel(r'HW3\IXI.xls', index_col=0)
print(type(df.at[12, 'AGE']))
