import numpy as np 
import pandas as pd
q6a = pd.Series(np.random.randint(0,2,1000))
q6b = pd.Series(np.random.randint(0,2,1000))
q7a = pd.Series(np.random.randint(0,2,1000))
q7b = pd.Series(np.random.randint(0,2,1000))
q8a = pd.Series(np.random.randint(0,2,1000))
q8b = pd.Series(np.random.randint(0,2,1000))
q9a = pd.Series(np.random.randint(0,2,1000))
q9b = pd.Series(np.random.randint(0,2,1000))
q10a = pd.Series(np.random.randint(0,2,1000))
q10b = pd.Series(np.random.randint(0,2,1000))
q11a = pd.Series(np.random.randint(0,2,1000))
q11b = pd.Series(np.random.randint(0,2,1000))
q12a = pd.Series(np.random.randint(0,2,1000))
q12b = pd.Series(np.random.randint(0,2,1000))
q13a = pd.Series(np.random.randint(0,2,1000))
q13b = pd.Series(np.random.randint(0,2,1000))
q14 = pd.Series(np.random.randint(0,11,1000))
q15 = pd.Series(np.random.randint(0,11,1000))
qa = q6a + q7a + q8a + q9a + q10a + q11a + q12a + q13a
qb = q6b + q7b + q8b + q9b + q10b + q11b + q12b + q13b

df3 = pd.DataFrame({
    'Location':'Sydney',
    'Timestamp':pd.Timestamp('20190412'),
    'Question6a':q6a,
    'Question6b':q6b,
    'Question7a':q7a,
    'Question7b':q7b,
    'Question8a':q8a,
    'Question8b':q8b,
    'Question9a':q9a,
    'Question9b':q9b,
    'Question10a':q10a,
    'Question10b':q10b,
    'Question11a':q11a,
    'Question11b':q11b,
    'Question12a':q12a,
    'Question12b':q12b,
    'Question13a':q13a,
    'Question13b':q13b,
    'Question14':q14,
    'Question15':q15,
    'Technical/Theorical mark':qb,
    'Pre/Exam mark':qa
})
print(df3)
print(df3.describe())
print(df3['Technical/Theorical mark'].value_counts())
print(df3['Pre/Exam mark'].value_counts())
df3.to_csv('./text data000.csv',index=False)