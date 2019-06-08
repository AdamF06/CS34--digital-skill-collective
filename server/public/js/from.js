var page_id;

function sub(){
    //age
    age_val = document.getElementsByName('age')[0].value

    //edu background
    background = document.getElementById('background')
    idx = background.selectedIndex
    background_val = background.options[idx].text;

    //skills
    skill = document.getElementById('skills')
    idx = skill.selectedIndex
    skill_val = skill.options[idx].text;

    //Q1.a
    q1_a = document.getElementsByName('q1_a')
    q1_a_val = parseInt(checkbox(q1_a))
    //Q1.b
    q1_b = document.getElementsByName('q1_b')
    q1_b_val = parseInt(checkbox(q1_b))

    //Q2.a
    q2_a = document.getElementsByName('q2_a')
    q2_a_val = parseInt(checkbox(q2_a))
    //Q2.b
    q2_b = document.getElementsByName('q2_b')
    q2_b_val = parseInt(checkbox(q2_b))

    //Q3.a
    q3_a = document.getElementsByName('q3_a')
    q3_a_val = parseInt(checkbox(q3_a))
    //Q3.b
    q3_b = document.getElementsByName('q3_b')
    q3_b_val = parseInt(checkbox(q3_b))

    //Q4.a
    q4_a = document.getElementsByName('q4_a')
    q4_a_val = parseInt(checkbox(q4_a))
    //Q4.b
    q4_b = document.getElementsByName('q4_b')
    q4_b_val = parseInt(checkbox(q4_b)) 

    //Q5.a
    q5_a = document.getElementsByName('q5_a')
    q5_a_val = parseInt(checkbox(q5_a))
    //Q5.b
    q5_b = document.getElementsByName('q5_b')
    q5_b_val = parseInt(checkbox(q5_b)) 

    //Q6.a
    q6_a = document.getElementsByName('q6_a')
    q6_a_val = parseInt(checkbox(q6_a))
    //Q6.b
    q6_b = document.getElementsByName('q6_b')
    q6_b_val = parseInt(checkbox(q6_b))

    //Q7.a
    q7_a = document.getElementsByName('q7_a')
    q7_a_val = parseInt(checkbox(q7_a))
    //Q7.b
    q7_b = document.getElementsByName('q7_b')
    q7_b_val = parseInt(checkbox(q7_b))

    //Q8.a
    q8_a = document.getElementsByName('q8_a')
    q8_a_val = parseInt(checkbox(q8_a))
    //Q8.b
    q8_b = document.getElementsByName('q8_b')
    q8_b_val = parseInt(checkbox(q8_b))

    q_a = [q1_a_val,q2_a_val,q3_a_val,q4_a_val,
        q5_a_val,q6_a_val,q7_a_val,q8_a_val]

    q_b = [q1_b_val,q2_b_val,q3_b_val,q4_b_val,
    q5_b_val,q6_b_val,q7_b_val,q8_b_val]

    // alert(q_a)
    // alert(q_b)
    
    
    $.ajax({
        type:"POST",
        url: '/form',
        //async:false,
        data:{   
            age : age_val,
            background : background_val,
            skill : skill_val,
            part_a : q_a,
            part_b : q_b
        },success:function(msg){
        if (msg) {
   
        }
    }});  
    setTimeout(function(){
        document.getElementById('show').disabled = false 
    },2000);
     
}

function show_result(){
    window.location = "/result"; 
}
function checkbox(_box){
    for (i=0; i<_box.length;i++){
        if(_box[i].checked){
            return _box[i].value
        }
    }
}

$(document).ready(function() { 
    page_id = 1;   
 });

 function next(){
    if(page_id<=3){
        page_id = page_id+1
        update(page_id)
    }
    // alert("current page is : "+page_id)
 }
function previous(){
    if(page_id>1){
        page_id = page_id-1
        update(page_id)
    }
}

function update(id){
    appear_id = 'part_'+id
    var group = document.getElementsByClassName('form-group')
    for(i=0;i<group.length;i++){
        group[i].style.display='none'
    }
    
    var show_group = document.getElementsByName(appear_id)
    // alert('there are'+show_group.length+' elements')
    for(i=0;i<show_group.length;i++){
        show_group[i].style.display='inline'
    }

    for(i=1;i<5;i++){
       
        document.getElementById('left-'+i).className='nav-link disabled'
    }
    for(i=1;i<=id;i++){
        document.getElementById('left-'+i).className='nav-link active'
    }
}