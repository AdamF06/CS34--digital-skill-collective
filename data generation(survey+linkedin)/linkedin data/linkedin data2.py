import numpy as np  
import pandas as pd 

a = pd.Series(np.random.randint(21,26,400))
b = pd.Series(np.random.randint(0,2,400))

df = pd.DataFrame({
    'Age':a,
    'Education':b 
})
print(df)
print(df['Age'].value_counts())
df.to_csv('./age 21-25.csv',index=False)