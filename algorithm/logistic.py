#%%
import numpy as np 
import pandas as pd 
import tensorflow as tf 

dataset = pd.read_csv('processed_data/new_category.csv')
dataset = dataset.sample(frac=1)

x_train = dataset.iloc[:,[0,1]]
label_data = dataset.iloc[:,[2]]
label_train = []

#convert intger classes into array
for i in range(len(label_data)):
    append_arr = [0,0,0,0]
    loc = int(label_data.iloc[i])
    append_arr[loc] = 1
    label_train.append(append_arr)

label_train = np.array(label_train)

#---------select 10% as test----------#
test_data = dataset.sample(frac=0.1)
x_test = test_data.iloc[:,[0,1]]
label_test_data = test_data.iloc[:,[2]]
label_test = []
for i in range(len(label_test_data)):
    append_arr = [0,0,0,0]
    loc = int(label_test_data.iloc[i])
    append_arr[loc] = 1
    label_test.append(append_arr)

label_test = np.array(label_test)

# print(x_test)
# print(label_test)
#%%
#dataset_0.label[dataset_0.loc[:,'label']!= 0] = 1

x = tf.placeholder('float', [None, 2])
y = tf.placeholder('float', [None, 4])

w = tf.Variable(tf.zeros([2,4]))
b = tf.Variable(tf.zeros([4]))

#multi-classification problem module
#output value 
#actv is a [1,4] matrix, represending the probability from category 0 to 3
#softmax is an activation function => compact element's value from the vector into 0-1 and the sum =1 

actv = tf.nn.softmax(tf.matmul(x,w)+b)

#log-loss
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(actv),reduction_indices=1))

learning_rate = 0.01
#optimization 
optm = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
#%%
#prediction, whether the output label is same as the real label
pred = tf.equal(tf.argmax(actv, 1), tf.argmax(y, 1))
#accuracy 
accr = tf.reduce_mean(tf.cast(pred, 'float'))
init = tf.global_variables_initializer()

#%%
training_epochs = 50
batch_size = 500
display_step = 5

sess = tf.Session()
sess.run(init)
for epoch in range(training_epochs):
    avg_cost = 0
    num_batch = int(len(dataset)/batch_size)

    for i in range(num_batch):
        start = i*batch_size
        end = (i+1)*batch_size

        batch_xs = x_train[start:end]
        batch_ys = label_train[start:end]

        #optimiz the cost, cost is y X actv ==> [1,10]*[10,1] ==> the score of prediction 
        sess.run(optm, feed_dict = {x: batch_xs, y:batch_ys})
        feeds = {x: batch_xs, y:batch_ys}
        #the average cost durning one epoch
        avg_cost += sess.run(cost, feed_dict = feeds)/num_batch


    #display 1 from every 5 peochs
    if epoch % display_step ==0:
        feeds_train = {x: batch_xs, y:batch_ys}
        feeds_test = {x: x_test, y:label_test}
        train_acc = sess.run(accr, feed_dict = feeds_train)
        test_acc = sess.run(accr, feed_dict = feeds_test)

        print("Epoch: %03d/%03d cost: %.9f train_acc: %.3f test_acc: %.3f"
             % (epoch, training_epochs, avg_cost, train_acc, test_acc))

print("Weight tensor is: ",sess.run(w))
print("bias tensor is: ",sess.run(b))

print('DONE')

