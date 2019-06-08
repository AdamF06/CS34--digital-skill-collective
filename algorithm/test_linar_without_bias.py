#%%
import numpy as np 
import tensorflow as tf 
import pandas as pd 
import matplotlib.pyplot as plt
dataset = pd.read_csv('processed_data/data_1000.csv')

#%%
#show data
#----------#
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

plt.figure(figsize=(15,12))
ax = plt.subplot()
ax.scatter(x1, y1, c = 'w', label= category[0])
ax.scatter(x2, y2, c = 'r', label= category[1])
ax.scatter(x3, y3, c = 'blue', label= category[2])
ax.scatter(x4, y4, c = 'green', label= category[3])

plt.show()

#%%
train_x = dataset.iloc[:,[2,4,6,8,10,12,14,16]]
train_y = dataset.iloc[:,[3,5,7,9,11,13,15,17]]
# print(type(train_x))
label_x = dataset['ABS1']
label_x = label_x[:,np.newaxis]

label_y = dataset['ABS2']
label_y = label_y[:,np.newaxis]
#%%
x = tf.placeholder(tf.float32,[None,8])
y = tf.placeholder(tf.float32,[None,1])
weight_x = tf.Variable(tf.ones([8,1]),dtype=tf.float32)
weight_y = tf.Variable(tf.ones([8,1]),dtype=tf.float32)
# bias = tf.Variable(tf.ones([1]),dtype=tf.float32)

# y_label = tf.add(tf.matmul(x,weight),bias)
perdict_x = tf.matmul(x,weight_x)
perdict_y = tf.matmul(x,weight_y)

loss_x = tf.reduce_mean(tf.square(y - perdict_x + tf.norm(weight_x,ord = 2)))
loss_y = tf.reduce_mean(tf.square(y - perdict_y + tf.norm(weight_y,ord = 2)))

training_rate = 0.0025

training_x_axis = tf.train.GradientDescentOptimizer(training_rate).minimize(loss_x)
training_y_axis = tf.train.GradientDescentOptimizer(training_rate).minimize(loss_y)

#check shape 
#---------#
print('x shape', x.shape)
print('y shape', y.shape)
print('weight shape', weight_x.shape)
# print('bias shape', bias.shape)

print('train_x shape', train_x.shape)
print('label_x shape', label_x.shape)
#%%
steps = 100
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(steps):      
        sess.run(training_x_axis,feed_dict={x:train_x, y:label_x})

        if(i%10==0):
            #loss contain L2 norm, real 
            current_loss = sess.run(loss_x,feed_dict={x:train_x, y:label_x})
            print("Loss is: ",current_loss)
    print("Weight for x axis ",sess.run(weight_x))
    np_weight_x = weight_x.eval()

error_x  = np.abs(np.dot(train_x,np_weight_x)-label_x)
print("Average error for X axis is:",np.mean(error_x))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(steps):      
        sess.run(training_y_axis,feed_dict={x:train_y, y:label_y})

        if(i%10==0):
            #loss contain L2 norm, real 
            current_loss = sess.run(loss_y,feed_dict={x:train_y, y:label_y})
            print("Loss is: ",current_loss)
    print("Weight for Y axis ",sess.run(weight_y))
    np_weight_y = weight_y.eval()

error_y  = np.abs(np.dot(train_y,np_weight_y)-label_y)
print("Average error for Y axis is:",np.mean(error_y))
