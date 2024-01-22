var ID=0;
$('body').ready(function(){
    console.log("students js is linked successfully");
    get_student_data();
    get_marks();
})
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

function CreateStudentTable(data, i){
    $(`#student_info_table`).append(`
              <tr>
                <td>${i+1}</td>
                <th scope="row" style="display:none;">${data.context[i].student_ID}</th>
                <td>${data.context[i].name}</td>
                <td>${data.context[i].roll_no}</td>
                <td>${data.context[i].mobile}</td>
                <td>${data.context[i].father_name}</td>
                <td>${data.context[i].mother_name}</td>
                <td>${data.context[i].father_mobile}</td>
                <td>
                  <button class="btn btn-dark mb-1" onclick="assign_marks('${data.context[i].student_ID}', '${data.context[i].name}')"><i class="fa-solid fa-pen"></i></button>
                </td>
              </tr>
    `)
}
var std_ID=0;
var std_name = "";
function assign_marks(student_ID, name){
    std_ID = student_ID;
    std_name = name;
    console.log(student_ID, name);
    $(`#student_name`).empty();
    $(`#student_name`).append(`
    ${name}
    `);    
}
function CreateMarksTable(data, i){
    var button;
    if(data.context[i].pass_fail == true){
        button = `
        <button class="btn btn-success"><i class="fa-solid fa-check"></i></button>
        `
    }
    else{
        button = `
        <button class="btn btn-danger"><i class="fa-regular fa-circle-xmark"></i></button>
        `
    
    }
    $(`#marks_info_table`).append(`
              <tr>
                <td>${i+1}</td>
                <td scope="row" style="display:none;">${data.context[i].marks_ID}</td>
                <td scope="row" style="display:none;">${data.context[i].student_id}</td>
                <td>${data.context[i].student_name}</td>
                <td>${data.context[i].science}</td>
                <td>${data.context[i].math}</td>
                <td>${data.context[i].computerScience}</td>
                <td>${data.context[i].Total_marks_per_subject}</td>
                <td>${data.context[i].Total_obtained_marks}</td>
                <td>${data.context[i].percentage}</td>
                <td>${data.context[i].passingPercentage}</td>
                <td>${button}</td>
                <td>
                  <button class="btn btn-dark mb-1" onclick="edit_marks('${data.context[i].marks_ID}', '${data.context[i].student_id}','${data.context[i].student_name}','${data.context[i].science}','${data.context[i].math}','${data.context[i].computerScience}','${data.context[i].Total_marks_per_subject}','${data.context[i].Total_obtained_marks}','${data.context[i].percentage}','${data.context[i].passingPercentage}','${data.context[i].pass_fail}')"><i class="fa-solid fa-pen"></i></button>
                  <button class="btn btn-danger mb-1" onclick="delete_marks_data('${data.context[i].marks_ID}')"><i class="fa-solid fa-trash"></i></button>
                </td>
              </tr>
    `)
}
$('body').on('click','#cancel_button',function(){
    reset_form();
});
function reset_form(){
    $(`#science`).val(null);
    $(`#math`).val(null);
    $(`#computerScience`).val(null);
    $(`#totalMarksPerSubject`).val(null);
    $(`#passingPercentage`).val(null);
    $(`#student_name`).empty();  
    $(`#student_name`).append(`Student's name`);  
}
/*using post method Get student info data from backend */
function get_student_data(){
    var get_url = get_data_url;
    fetch(get_url, {
        method : "POST",
        credentials : "same-origin",
        headers:{
            "X-Requested-With" : "XMLHttpRequest",
            "X-CSRFToken" : getCookie("csrftoken"),
        }
    })
    .then(
        response => response.json()
    )
    .then(
        data => {
            // console.log(data);
            // console.log(data.context[0].name);
            // console.log(data.context.length);
            $(`#student_info_table`).empty();
            console.log(`get data function was called`);
            console.log(data);
            for( var i=0;i<data.context.length;i++){
                CreateStudentTable(data, i);
            }
        }
    );
}
/*using post method Get student info data from backend */

/* insert marks using post method fetch api starts */
$('body').on('click','#submit_button',function(){
    if(Number($(`#marks_ID_`).text())!=0){
        update_marks_data();
        reset_form();
        console.log('update marks');
        console.log(Number($(`#marks_ID_`).text()));
    }
    else{
        insert_marks();
        console.log('insert marks');
        console.log(Number($(`#marks_ID_`).text()));
        reset_form();
    }    
})
function insert_marks(){
    var insert_data_url = insert_marks_url;
    if($(`#science`).val() == "" || $(`#math`).val() == "" || $(`#computerScience`).val() == "" || $(`#totalMarksPerSubject`).val() == "" || $(`#passingPercentage`).val() == ""){
        alert("Input fields can'be empty");
    }
    else{
        if($.isNumeric($(`#science`).val()) || $.isNumeric($(`#math`).val()) || $.isNumeric($(`#computerScience`).val()) || $.isNumeric($(`#totalMarksPerSubject`).val()) || $.isNumeric($(`#passingPercentage`).val())){
                    //post data to the backend
                    var data = new Object()
                    data.student_ID = Number(std_ID)
                    data.student_name = std_name
                    data.science = $(`#science`).val()
                    data.math = $(`#math`).val()
                    data.computerScience = $(`#computerScience`).val()
                    data.totalMarksPerSubject = $(`#totalMarksPerSubject`).val()
                    data.passingPercentage = $(`#passingPercentage`).val()
                    console.log(data);

                    fetch(
                        insert_data_url,
                        {
                            method : "POST",
                            credentials : "same-origin",
                            headers:{
                                "X-Requested-With" : "XMLHttpRequest",
                                "X-CSRFToken" : getCookie("csrftoken"),
                            },
                            body : JSON.stringify({payload:data})
                        }
                    ).then(
                        response => response.json()
                    )
                    .then(
                        data => {
                            console.log(data);
                            get_marks();
                            $(`#student_name`).empty();
                            $(`#student_name`).append(`student's name`);
                            std_ID = 0;
                            std_name = "";
                        }
                    )
        }
        else{
            alert("enter numeric values in the input fields");
        }
    }
}
/* insert marks using post method fetch api ends */

/* get data using post method starts */
function get_marks(){
    var get_marks_url = get_marks_data_url;
    fetch(
        get_marks_url,
        {
            method : "POST",
            credentials : "same-origin",
            headers:{
                "X-Requested-With" : "XMLHttpRequest",
                "X-CSRFToken" : getCookie("csrftoken"),
            }
        }
    ).then(
        response => response.json()
    ).then(
        data =>{
            console.log(data);
            // console.log(data.context.length);
            // console.log(data.context[i].student_id);
            $(`#marks_info_table`).empty();
            for( var i=0;i<data.context.length;i++){
                CreateMarksTable(data, i);
            }
        }
    )
}
/* get data using post method ends */

/* update data using post method fetch api starts */
function edit_marks(marks_ID, student_ID, student_name,science, math, computerScience, Total_marks_per_subject, Total_obtained_marks, percentage, passingPercentage, pass_fail){
console.log("get_marks function called");
console.log(marks_ID, student_ID, student_name,science, math, computerScience, Total_marks_per_subject, Total_obtained_marks, percentage, passingPercentage, pass_fail);
$(`#student_name`).empty();
$(`#student_name`).append(`
   student_name
`);
$(`#marks_ID_`).empty();
$(`#marks_ID_`).append(marks_ID);
//update information in the form about the select student's marks
$(`#science`).val(science)
$(`#math`).val(math)
$(`#computerScience`).val(computerScience)
$(`#totalMarksPerSubject`).val(Total_marks_per_subject)
$(`#passingPercentage`).val(passingPercentage)
}
function update_marks_data(){
    var update_data_url = update_marks_data_url;
    if($(`#science`).val() == "" || $(`#math`).val() == "" || $(`#computerScience`).val() == "" || $(`#totalMarksPerSubject`).val() == "" || $(`#passingPercentage`).val() == ""){
        alert("Input fields can'be empty");
    }
    else{
        if($.isNumeric($(`#science`).val()) || $.isNumeric($(`#math`).val()) || $.isNumeric($(`#computerScience`).val()) || $.isNumeric($(`#totalMarksPerSubject`).val()) || $.isNumeric($(`#passingPercentage`).val())){
                    //post data to the backend
                    var data = new Object()
                    data.marks_ID = Number($(`#marks_ID_`).text())
                    data.science = $(`#science`).val()
                    data.math = $(`#math`).val()
                    data.computerScience = $(`#computerScience`).val()
                    data.totalMarksPerSubject = $(`#totalMarksPerSubject`).val()
                    data.passingPercentage = $(`#passingPercentage`).val()
                    console.log(data);
                    fetch (update_data_url,
                        {
                            method:"POST",
                            credentials:"same-origin",
                            headers:{
                                "X-Requested-With" : "XMLHttpRequest",
                                "X-CSRFToken" : getCookie("csrftoken"),
                            },
                            body:JSON.stringify({payload : data})
                        }
                        ).then(
                            response=>response.json()
                        ).then(
                            data=>{
                                console.log(data);
                                get_marks();
                                $(`#marks_ID_`).empty();
                            }
                        )      
        }
        else{
            alert("enter numeric values in the input fields");
        }
    }
}
/* update data using post method fetch api ends */

/* delete data using post method starts */
function delete_marks_data(ID){
var delete_data_url = delete_marks_data_url;
var data = {
    marks_ID : ID
}
var choice = confirm("Are you sure you want to delete this record?");
if(choice==true){
    fetch(delete_data_url,
        {
            method:"POST",
            credentials : "same-origin",
            headers:{
                "X-Requested-With" : "XMLHttpRequest",
                "X-CSRFToken" : getCookie("csrftoken"),
            },
            body : JSON.stringify({payload:data})
        }).then(response=>response.json())
        .then(
            data=>{
                console.log(data);
                get_marks();
                get_student_data();
                ID=0;
            }
        )
}
}
/* delete data using post method ends */