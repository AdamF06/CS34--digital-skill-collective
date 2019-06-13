# CS34--digital-skill-collective
## Required package

*** *** ***
Inside python 3.7.3:
    TensorFlow 2.0
    Pandas 2.8.0
    Numpy 1.16.2 

NodeJs 11.11.0
    all related packages were uploaded in node_modules  
*** *** ***
###NOTE
    The package used for connecting python to javascript is "python shell" which can get out put from python shell. However, in different machine the output from python shell may be different (in title), so you may do some little changes on your computer  @Jamie.

## File structure
There are two floders representing two parts:
Server is for the system and Algorithm is for offline training.

Inside algorithm folder, actually, there are only two files used in the system: which are "test_linar_without_bias.py" for prediction personality and "logistic.py" for classfication. 

"classification.py" and "classification_manual.py" are implementation of nueral network both of them have very low accuarcy which is 33%, maybe NN is not suitable for our data model.But I leaved them here for your interest @Jamie. 

KNN filter needn't training and It is within the Node server.

all the dummy data we used is stored in 'processed_data' folder. It is fine if you want to replace them.

## HOW TO USE
Run pyhton files firstly, then you can get weight sets from the out put. And then copy the weight set into the file 'integration.py' which is located at server->model->'integration.py'.

Then  move to server folder and strating server by command:
    node server.js
then you can access from local port 3000 by typing following url in your browser "127.0.0.1/3000"

