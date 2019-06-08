import numpy as np 
import pandas as pd 
import tensorflow as tf 
import sys

if  __name__ == "__main__":
    edu_list={
        'Postgraduate' : 0,
        'Undergraduate' : 1,
        'High School' : 2,
    }

    skill_list={
        'Management':1, 'Programming':2, 'Web':3,
        'Andorid':4, 'Big data':5, 'Data analysis':6,
        'Data Integration':7, 'Database':8, 'Design':9, 'Java':10,
        'Machine Learning':11,'Marketing':12,'Microstrategy':13,
        'Python':14,'Software Requirements':15,
        'Software Testing':16,'SQL':17,'None':18
    }
    #Get first four items
    #following is a example

    age = int(sys.argv[1]) 
    edu = sys.argv[2]
    skill = sys.argv[3]
    part_a = sys.argv[4]
    part_b = sys.argv[5]
    # print("type of questions: ",type(part_a[1]))

    edu_N = edu_list[edu]
    skill_N = skill_list[skill]
    question_part_a =[]
    question_part_b =[]

    for i in part_a:
        if i != ',':
            question_part_a.append(int(i))
            # print(int(i),'type is',type(int(i)))

    for i in part_b:
        if i != ',':
            question_part_b.append(int(i))

    #Linar regression Function
    #weight is calculated after training 
    #shape => (8,1)
    weight_x =  np.array([[1.1584679],
        [1.1435739],
        [1.1198521],
        [1.0866346],
        [1.1265752],
        [1.1516919],
        [1.1382508],
        [1.1365937]])
    weight_y = np.array([[1.1157205],
        [1.1127706],
        [1.0842019],
        [1.1628593],
        [1.1142836],
        [1.2027415],
        [1.143562 ],
        [1.1635718]])

    #reset 16 questions into two array,only 0 or 1 
    #shape => (1,8)
    question_part_a = np.array(question_part_a)
    question_part_b = np.array(question_part_b)

    X = np.dot(question_part_a, weight_x)
    Y = np.dot(question_part_b, weight_y)
    #X,Y is personality
    #print(X,Y)

    person_mark = np.array([[X[0],Y[0]]])

    #Logistc classification
    #get from off line training 
    weight_logs = np.array([[0.26726398,0.04499606,-0.27126253,-0.04099749],
    [-0.27459967,0.02630348,0.27640593,-0.02810961]])

    bias = np.array([[0.00082212,-0.06045728,0.00041817,0.05921698]])

    actv = tf.nn.softmax(tf.matmul(person_mark,weight_logs)+bias)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    category_ = sess.run(tf.argmax(actv,1))[0]
    category_np = np.array([category_])
    per_ = sess.run(actv)
    # print("Prediction is: ",sess.run(actv))
    # print('class is ',category_)
    
    category = int(category_np)
    # print(category)

    #Fliter
    #---# If a high student
    course_list = pd.read_excel('data/course_list.xlsx')
    dataset = pd.read_excel('data/LinkedIn.xlsx')
    data = dataset[dataset.Major_list == category]

    if edu_N == 2:
        #recomand some beginner courses  
        course_list = course_list[course_list.Cate_No == category]
        course_list = course_list[0:3]

        result =[]
        for i in range(3):
            result.append(course_list.loc[i:i].Course_No.tolist())

        print(per_,"|",category_,'|',result,'|',X[0],'|',Y[0])       
    else:  

        x_train = data.loc[:,['Age','Major_list','Edu_list','Skills1-N']]
        label_train = data['Course-N']

        student = [age,category,edu_N,skill_N]

        # print(x_train.shape)
        # print(label_train.shape)
        xtr = tf.placeholder(tf.float32, [None, 4])
        xte = tf.placeholder(tf.float32, [4])

        distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
        #find 3 nearnest student
        pred = tf.nn.top_k(-distance, 6).indices
        init = tf.global_variables_initializer()

        with tf.Session() as sess:
            sess.run(init)
            nn_index = sess.run(pred, feed_dict={xtr: x_train, xte: student})
            result=[]
            for i in nn_index:
                result_df = course_list[course_list.Course_No == int(label_train.iloc[i])]
                result.append(result_df['Course_No'].tolist())
                # print(result_df['Course_Name'].tolist())        
                # print("Prediction of student are: ",label_train.iloc[i])
            print(per_,"|",category_,'|',result,'|',X[0],'|',Y[0])