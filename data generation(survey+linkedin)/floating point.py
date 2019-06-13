import numpy as np 
import pandas as pd 
a = pd.Series(np.random.uniform(-1.6,1.6,1000))
b = pd.Series(np.random.uniform(-1.6,1.6,1000))
df = pd.DataFrame({
'T1 Floating':a,
'T2 Floating':b
})
print(df)
df.to_csv('./floating data.csv',index=False)