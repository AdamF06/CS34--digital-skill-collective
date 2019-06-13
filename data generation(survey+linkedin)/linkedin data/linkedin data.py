import numpy as np  
import pandas as pd 

a = pd.Series(np.random.randint(18,21,300))
b = pd.Series(np.random.randint(0,2,300))

df = pd.DataFrame({
    'Age':a,
    'Education':b
})
print(df)
print(df['Age'].value_counts())
df.to_csv('./age 18-20.csv',index=False)