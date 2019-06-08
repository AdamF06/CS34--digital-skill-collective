#%%
import numpy as np 
import pandas as pd 
import tensorflow as tf 

#student's category classfied by previous stage 
category = 0
dataset = pd.read_excel('processed_data/prLinkedIn.xlsx')
data = dataset[dataset.Major_list == category]

x_train = data.loc[:,['Age','Major_list','Edu_list','Skills1-N']]
label_train = data['Course-N']

print(x_train.shape)
print(label_train.shape)

rand_row = np.random.randint(len(data))
test = x_train.iloc[rand_row]

#%%
xtr = tf.placeholder(tf.float32, [None, 4])
xte = tf.placeholder(tf.float32, [4])

distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
#find 3 nearnest student
pred = tf.nn.top_k(-distance, 3).indices
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    nn_index = sess.run(pred, feed_dict={xtr: x_train, xte: test}) 
    for i in nn_index:
        print("Prediction of student ", rand_row,'are: ',label_train.iloc[i])


#%%
print(label_train.iloc[rand_row])