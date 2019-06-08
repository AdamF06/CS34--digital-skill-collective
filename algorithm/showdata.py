#%%
import numpy as np 
import tensorflow as tf 
import pandas as pd 
import matplotlib.pyplot as plt

dataset = pd.read_csv('processed_data/data_1000.csv')
# print(dataset)
category = ['IT Management', 'Social marketing',
'Design Skills', 'software engineering']
x1 = dataset[dataset.Category == category[0]]['ABS1']
y1 = dataset[dataset.Category == category[0]]['ABS2']

x2 = dataset[dataset.Category == category[1]]['ABS1']
y2 = dataset[dataset.Category == category[1]]['ABS2']

x3 = dataset[dataset.Category == category[2]]['ABS1']
y3 = dataset[dataset.Category == category[2]]['ABS2']

x4 = dataset[dataset.Category == category[3]]['ABS1']
y4 = dataset[dataset.Category == category[3]]['ABS2']

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.scatter(x1, y1, c = 'w', label= category[0])
ax.scatter(x2, y2, c = 'r', label= category[1])
ax.scatter(x3, y3, c = 'blue', label= category[2])
ax.scatter(x4, y4, c = 'green', label= category[3])

plt.show()
