import pandas as pd 
df = pd.read_csv('category.csv')
print(df)
b = df.loc['ABS1']
print(b)