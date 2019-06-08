const {PythonShell} = require("python-shell");
var fs = require("fs");
var cate_list = ['IT Management','Social marketing',
'software engineering','Design Skills']

var index_list = [0,1,2,3]

exports.showHomePage = function(req,res){
    res.render('home.ejs',{})
}
exports.showForm = function(req,res){
    res.render('test.ejs',{})
}
exports.showResult = function(req,res){
    age = req.body.age
    background = req.body.background
    skill = req.body.skill
    part_a = req.body.part_a
    part_b = req.body.part_b

    let options = {
    mode: 'text',
    pythonPath: '/Users/yuexiaopeng/anaconda3/bin/python3',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: './model/',
    args: [age,background,skill,part_a,part_b]
    };

    var test = new PythonShell('integration.py',options)
    test.on('message',function(message){
        console.log('this is messgae\n====='+message)
        var data = message;
        fs.writeFile("./input_data/input_data.txt",data,function(err){
			if(err){
				res.end(err);
			}
		});
    });

    test.end(function (err,code,signal) {
        if (err) throw err;
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        console.log('finished');
      });
  
}

exports.getResult = function(req,res){
    var data=fs.readFileSync("./input_data/input_data.txt","utf-8");

    arr = data.split('|')
    for (i=0;i<arr.length;i++){
        arr[i] = arr[i].replace(/'/g, "");
        arr[i] = arr[i].replace(/"/g, "");
        arr[i] = arr[i].replace(/\[|]/g,'');
        
        arr[i] = arr[i].replace(/,/g,'|');
    }
    arr[0]=arr[0].replace(/ /g, "|");
    console.log('Result received is :*** \n'+arr)
    percentage = arr[0].split('|')
    percentage.splice(4,1)
    category = parseInt( arr[1])    
    courses = arr[2].split('|')
    courses = removeRepeat(courses)
   
    X = parseFloat(arr[3])
    Y = parseFloat(arr[4])

    console.log("percentage array is:*** \n",percentage)
    console.log('category is:*** \n',category)
    console.log('courses are:*** \n',courses)
  
    console.log("X is:*** \n",X)
    console.log('Y is:*** \n',Y)
    
    var file="data/des.json";
    var json_data=JSON.parse(fs.readFileSync(file));
    course_1_id =parseInt(courses[0])-1
    course_2_id =parseInt(courses[1])-1
    course_3_id =parseInt(courses[2])-1

    index_list.splice(category,1)
  res.render('result.ejs',{
    'category':cate_list[category], 
    'course_1':json_data[course_1_id].Course_Name,
    'course_2':json_data[course_2_id].Course_Name,
    'course_3':json_data[course_3_id].Course_Name,
    'des_1':json_data[course_1_id].Des,
    'des_2':json_data[course_2_id].Des,
    'des_3':json_data[course_3_id].Des,

    'percent':parseFloat(percentage[category]).toFixed(2)*100+'%',

  
    'pe_1':parseFloat(percentage[index_list[0]]).toFixed(2)*100+'%',
    'pe_2':parseFloat(percentage[index_list[1]]).toFixed(2)*100+'%',
    'pe_3':parseFloat(percentage[index_list[2]]).toFixed(2)*100+'%',
 
    'option1':cate_list[index_list[0]],
    'option2':cate_list[index_list[1]],
    'option3':cate_list[index_list[2]],   
    })
}

exports.showMore = function(req,res){
    var file="data/des.json";
    var json_data=JSON.parse(fs.readFileSync(file));
    res.render('more_res.ejs',{

        'course_1':json_data[20].Course_Name,
        'course_2':json_data[33].Course_Name,
        'course_3':json_data[7].Course_Name,
        'course_4':json_data[5].Course_Name,
        'course_5':json_data[9].Course_Name,
        'course_6':json_data[11].Course_Name,


        'des_1':json_data[20].Des,
        'des_2':json_data[33].Des,
        'des_3':json_data[7].Des,
        'des_4':json_data[5].Des,
        'des_5':json_data[9].Des,
        'des_6':json_data[11].Des,
    })
}



function removeRepeat(array){
    var n = [];
    for(var i = 0; i < array.length; i++){
      if (n.indexOf(array[i]) == -1) n.push(array[i]);
    }
    return n;
  }