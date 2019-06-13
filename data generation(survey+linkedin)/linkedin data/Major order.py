import numpy as np  
import pandas as pd 

a = pd.Series(np.random.randint(1,10,700))


df = pd.DataFrame({
    'Major':a
})
print(df)
print(df['Major'].value_counts())
df.to_csv('./major order700.csv',index=False)