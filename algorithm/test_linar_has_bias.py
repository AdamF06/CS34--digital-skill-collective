#%%
import numpy as np 
import tensorflow as tf 
import pandas as pd 
import matplotlib.pyplot as plt
dataset = pd.read_csv('data_1000.csv')

#%%
#show data
#----------#
# print(dataset)
# label_x = dataset['ABS1']
# label_y = dataset['ABS2']
# x_point = [v for v in label_x]
# y_point = [v for v in label_y]
# plt.figure(figsize=(15,12))
# plt.scatter (x_point, y_point, c='w')
# plt.show()

#%%
train_x = dataset.iloc[:,[2,4,6,8,10,12,14,16]]
# print(type(train_x))
label_x = dataset['ABS1']
label_x = label_x[:,np.newaxis]
#%%
x = tf.placeholder(tf.float32,[None,8])
y = tf.placeholder(tf.float32,[None,1])
weight = tf.Variable(tf.ones([8,1]),dtype=tf.float32)
bias = tf.Variable(tf.ones([1]),dtype=tf.float32)

print(weight, bias)

y_label = tf.add(tf.matmul(x,weight),bias)
loss = tf.reduce_mean(tf.square(y - y_label + tf.norm(weight,ord = 2)))
training_rate = 0.005

train = tf.train.GradientDescentOptimizer(training_rate).minimize(loss)

#check shape 
#---------#
print('x shape', x.shape)
print('y shape', y.shape)
print('weight shape', weight.shape)
print('bias shape', bias.shape)

print('train_x shape', train_x.shape)
print('label_x shape', label_x.shape)
#%%
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3000):      
        sess.run(train,feed_dict={x:train_x, y:label_x})

        if(i%100==0):
            print(sess.run(loss,feed_dict={x:train_x, y:label_x}))
    print(sess.run(weight),sess.run(bias))


