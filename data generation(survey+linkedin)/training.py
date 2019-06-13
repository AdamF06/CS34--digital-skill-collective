import numpy as np 
import pandas as pd 
dates = pd.date_range('20160101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
df2 = pd.DataFrame({'Question1':1.,
'Question2':pd.Timestamp(20130102),
'Question3':pd.Series(1, index=list(range(4)), dtype='float32'),
'Question4':np.array([3]*4, dtype='int32'),
'Question5':pd.Categorical(['test','train','test','train']),
'Question6':'foo'
})
print(df2)
print(df2.describe())
print(df2['Question5'].value_counts())