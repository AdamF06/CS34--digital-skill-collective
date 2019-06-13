import numpy as np 
import pandas as pd 
a = np.random.randint(0,9)
a1 = pd.Series(np.random.randint(0,9,10))
b = np.random.randint(0,9)
b1 = pd.Series(np.random.randint(0,9,10))
print('('f'{a}'','f'{b}'')')

if a <= 4:
    if b > 4:
        c = 'Software Enginerring'
    else:
        c = 'Social marketing'
if a > 4:
    if b > 4: 
        c = 'Design skills'
    else:
        c = 'IT management'

print(c)
df = pd.DataFrame({
    'T/T mark':a1,
    'P/E mark':b1,
    'Recommend':c
})
print(df)