ID=0;
/* miscellanious code related to the page starts */
$('body').on('click','#cancel_button',function(){
    reset_form();
})
function reset_form(){
    $('#name').val("");
    $('#roll_no').val("");
    $('#mobile').val("");
    $('#father_name').val("");
    $('#mother_name').val("");
    $('#father_mobile').val("");
    ID=0;
}

//get csrf token
//get CSRF Token from the cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
/* miscellanious code related to the page ends */

/* Insert , Update Data starts */
$(`body`).on(`click`,'#submit_button', function(){
    if(ID!=0){
        if($('#name').val()=="" || $('#roll_no').val()=="" || $('#mobile').val()=="" || $('#father_name').val()=="" || $('#mother_name').val()=="" || $('#father_mobile').val()=="")
        {
            alert("input fields can not be empty");
        }
        else{
            Update_Data();
            console.log('data update function called');
        }
    }
    else{
        if($('#name').val()=="" || $('#roll_no').val()=="" || $('#mobile').val()=="" || $('#father_name').val()=="" || $('#mother_name').val()=="" || $('#father_mobile').val()=="")
        {
            alert("input fields can not be empty");
        }
        else{
            Insert_data();
            console.log('data insert function called');
        }
    }
})
function Insert_data(){
    var data = new Object();
    data.student_name = $('#name').val();
    data.roll_no = $('#roll_no').val();
    data.mobile = $('#mobile').val();
    data.father_name = $('#father_name').val();
    data.mother_name = $('#mother_name').val();
    data.father_mobile = $('#father_mobile').val();
    console.log(data)
    fetch(
        insert_student_info,{
            method:'POST',
            credentials:'same-origin',
            headers:{
                'X-Requested-With' : 'XMLHttpRequest',
                "X-CSRFToken" : getCookie("csrftoken"),
            },
            body : JSON.stringify({payload:data})
        }
    ).then(
        response => response.json()
    ).then(
        data=>{
            console.log(data);
            get_data();
            reset_form();
        }
    )
}
function populate_form(student_ID, student_name, roll_no, mobile, father_name, mother_name, father_mobile){
    ID=student_ID;
    $('#name').val(student_name);
    $('#roll_no').val(roll_no);
    $('#mobile').val(mobile);
    $('#father_name').val(father_name);
    $('#mother_name').val(mother_name);
    $('#father_mobile').val(father_mobile);
}
function Update_Data(){
    if($('#name').val()=="" || $('#roll_no').val()=="" || $('#mobile').val()=="" || $('#father_name').val()=="" || $('#mother_name').val()=="" || $('#father_mobile').val()==""){
        alert("input fields cannot be empty");
    }
    else{
        var data ={
            student_ID : ID,
            student_name : $('#name').val(),
            roll_no : $('#roll_no').val(),
            mobile : $('#mobile').val(),
            father_name : $('#father_name').val(),
            mother_name : $('#mother_name').val(),
            father_mobile : $('#father_mobile').val(),
        }
        fetch(
            Update_student_info,
            {
                method : "POST",
                credentials : "same-origin",
                headers:{
                    "X-Requested-With" : "XMLHttpRequest",
                    "X-CSRFToken" : getCookie("csrftoken"),
                },
                body : JSON.stringify({payload : data})
            }
        ).then(
            response => response.json()
        )
        .then(
            data=>{
                console.log(data);
                get_data();
                ID=0;
            }
        );
    }
}
/* Insert , Update Data ends */

/* Read data and show it in the table starts */
$('body').ready(function(){
    get_data();
})
function CreateTable(data,i){
    $(`#student_info_table`).append(`
    <tr>
    <td>${i}</td>
    <td scope="row" style="display:none;">${data.context[i].student_ID}</td>
    <td>${data.context[i].student_name}</td>
    <td>${data.context[i].roll_no}</td>
    <td>${data.context[i].mobile}</td>
    <td>${data.context[i].father_name}</td>
    <td>${data.context[i].mother_name}</td>
    <td>${data.context[i].father_mobile}</td>
    <td>
      <button class="btn btn-dark mb-1" onclick="populate_form('${data.context[i].student_ID}', '${data.context[i].student_name}','${data.context[i].roll_no}', '${data.context[i].mobile}', '${data.context[i].father_name}', '${data.context[i].mother_name}', '${data.context[i].father_mobile}')"><i class="fa-solid fa-pen"></i></button>
      <button class="btn btn-danger mb-1" onclick="delete_data('${data.context[i].student_ID}')"><i class="fa-solid fa-trash"></i></button>
    </td>
  </tr>
    `)
}
function get_data(){
    fetch(
        Read_student_info,{
            method : 'POST',
            credentials : "same-origin",
            headers : {
                'X-Requested-With' : 'XMLHttpRequest',
                "X-CSRFToken" : getCookie("csrftoken"),
            }
        }
    ).then(
        response => response.json()
    ).then(
        data => {
            $('#student_info_table').empty()
            for(var i=0;i<data.context.length;i++){
                CreateTable(data,i);
            }
        }
    );
}
/* Read data and show it in the table ends */

/* Delete Data starts */
function delete_data(ID){
    var data = {
        student_ID : ID
    }
    var choice = confirm("are you sure you want to delete this record?");
    if(choice==true){
        fetch(delete_student_info,
            {
                method : "POST",
                credentials : "same-origin",
                headers:{
                    "X-Requested-With" : "XMLHttpRequest",
                    "X-CSRFToken":getCookie("csrftoken"),
                },
                body:JSON.stringify({payload:data})
            }
            ).then(
                response=>response.json()
            )
            .then(
                data=>{
                    console.log(data);
                    get_data();
                    ID=0;
                }
            );
    }
}
/* Delete Data ends */