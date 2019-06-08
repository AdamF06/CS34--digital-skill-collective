#%%
import tensorflow as tf
import numpy as np
import pandas as pd 

dataset = pd.read_csv('processed_data/new_category.csv')
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

#random select 10% from training set as cross testing data
test_idx = np.random.randint(len(label_train), size=100)

x_test = x_train.iloc[test_idx,:]
label_test = label_train[test_idx,:]
print(x_test)

#%%
#----------#
#two layers designed in here
#layer1 ==> [2,8]
#layer2 ==> [8,4]
#each layer is a linear combination: Wx+b, W is the primiter aimed to
#be optimized, b is bias and x is the input.
#And it will go through an activation function δ
#Output = δ(Wx+b), the AF used here is the sigmoid function
#----------#
hidden1 = 2
hidden2 = 2
n_input = 2
n_classes = 4

x = tf.placeholder('float',[None,n_input])
y = tf.placeholder('float',[None,n_classes])

stddev = 0.1
weights = {
    'w1':tf.Variable(tf.random_normal([n_input,hidden1],stddev = stddev)),   
    'w2':tf.Variable(tf.random_normal([hidden1,hidden2],stddev = stddev)),
    'out':tf.Variable(tf.random_normal([hidden2,n_classes],stddev = stddev)),   
}


def multilayer_preceptron(_x, _weights):
    layer1 = tf.nn.sigmoid(tf.matmul(_x, _weights['w1']))
    layer2 = tf.nn.sigmoid(tf.matmul(layer1, _weights['w2']))
    return (tf.matmul(layer2,_weights['out']))

prediction = multilayer_preceptron(x, weights)

#%%
#Loss function = cross entropy
#In general, cross entropy used to measure the differentiation between
#two matrixs, is the sum of -p*log(q), pq are victors from two matrix 
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = prediction,labels = y))
#optimization 
optm = tf.train.GradientDescentOptimizer(learning_rate = 0.0025).minimize(cost)

corr = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accr = tf.reduce_mean(tf.cast(corr, 'float'))

init = tf.global_variables_initializer()

#iteration 50 times
#batch size is 100

training_epochs = 100
batch_size = 250
display_step = 10

sess = tf.Session()
sess.run(init)
for epoch in range(training_epochs):
    avg_cost = 0

    total_batch = int(len(dataset)/batch_size)
    for i in range(batch_size):
        idx = np.random.randint(len(label_train), size=batch_size)
        batch_xs = x_train.iloc[idx,:]
        batch_ys = label_train[idx,:]
        #optimiz the cost, 
        sess.run(optm, feed_dict = {x: batch_xs, y:batch_ys})
        feeds = {x: batch_xs, y:batch_ys}
        #the average cost durning one epoch
        avg_cost += sess.run(cost, feed_dict = feeds)/batch_size
    avg_cost = avg_cost / total_batch
    
    #display 1 from every 4 peochs
    if epoch % display_step ==0:
        print('Epoch: %03d/%03d cost: %.9f' % (epoch,training_epochs,avg_cost))
        feeds = {x: batch_xs, y:batch_ys}
        train_acc = sess.run(accr, feed_dict = feeds)
        print('Train Accuracy: %.3f' % (train_acc))
        feeds = {x: x_test, y:label_test}
        test_acc = sess.run(accr, feed_dict = feeds)
        print('Test Accuracy: %.3f' % (test_acc))
print('DONE')
#%%
print('test')
student =[[1.1, 2.3],[8.2,7.6],[1.2,7.3],[7.3, 1.6]]
print(multilayer_preceptron(student, weights).eval(session = sess))