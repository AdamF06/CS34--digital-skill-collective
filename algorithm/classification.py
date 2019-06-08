#%%
import tensorflow as tf
import tensorflow.contrib.eager as tfe
import pandas as pd

tf.enable_eager_execution()

data_path = 'new_category.csv'
column_names = ['ABS1','ABS2','label']
feature_names = column_names[:-1]
label_name = column_names[-1]

batch_size = 64

#shauffle == true randomly pick data (row) 
train_dataset = tf.contrib.data.make_csv_dataset(
    data_path,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1)

features, labels = next(iter(train_dataset))
# print(features)
# print(labels)

#%%
def pack_features_vector(features, labels):
#   Pack the features into a single array.
    features = tf.stack(list(features.values()), axis=1)
    return features, labels

#using MAP method to compact fatures with it into training data set

train_dataset = train_dataset.map(pack_features_vector)

features, labels = next(iter(train_dataset))
# print(features)
# print(labels)

#%%
#NN network for four-classification 
#input is [None,2]
#first layer is [2,8]
#second layer is [8,4]
#output is [None,4]
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation=tf.nn.relu, input_shape=(2,)),  # input shape required
    tf.keras.layers.Dense(16, activation=tf.nn.relu),
    tf.keras.layers.Dense(4)
])

# predictions = model(features)

# tf.nn.softmax(predictions[:5])

# print("Prediction: {}".format(tf.argmax(predictions, axis=1)))
# print("    Labels: {}".format(labels))

#%%
def loss(model, x, y):
    y_ = model(x)
    return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)

l = loss(model, features, labels)
#print("Loss test: {}".format(l))

#%%
# Gradient optimization function 
def grad(model, inputs, targets):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, targets)
    return loss_value, tape.gradient(loss_value, model.trainable_variables)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

global_step = tf.train.get_or_create_global_step()

#%%
train_loss_results = []
train_accuracy_results = []

num_epochs = 501

for epoch in range(num_epochs):
    epoch_loss_avg = tfe.metrics.Mean()
    epoch_accuracy = tfe.metrics.Accuracy()

# Training loop - using batches of 64
    for x, y in train_dataset:
    # Optimize the model
        loss_value, grads = grad(model, x, y)
        optimizer.apply_gradients(zip(grads, model.variables),
                            global_step)

        # Track progress
        epoch_loss_avg(loss_value)  # add current batch loss
        # compare predicted label to actual label
        epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

    # end epoch
    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 50 == 0:
        print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                epoch_loss_avg.result(),epoch_accuracy.result()))

#%%
#Test
#----#

label_names = ['IT Management', 'Social marketing', 'software engineering', 'Design Skills']
student1 = [1.1,1.1]
student2 = [5.6,1.1]
student3 = [1.1,9.1]

predict_dataset = tf.convert_to_tensor([student1,student2,student3])

for i, logits in enumerate(predict_dataset):
    label_idx = tf.argmax(logits).numpy()
    p = tf.nn.softmax(logits)[label_idx]
    name = label_names[label_idx]
    print("Students {} prediction: {} ({:4.1f}%)".format(i, name, 100*p))