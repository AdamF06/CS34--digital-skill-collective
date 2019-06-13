import numpy as np  
import pandas as pd 

a = pd.Series(np.random.randint(26,31,300))
b = pd.Series(np.random.randint(0,2,300))

df = pd.DataFrame({
    'Age':a,
    'Education':b 
})
print(df)
print(df['Age'].value_counts())
df.to_csv('./age 26-30.csv',index=False)