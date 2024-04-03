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
  $('body').ready(function(){
    $('#change_title_of_form').empty()
    $('#change_title_of_form').text("Create")
    get_students_for_select_input()
    get_marks_data()
  })

//**** SELECT STUDENT DROPDOWN MENU STARTS****
  function get_students_for_select_input(){
    fetch(
        StudentAPI_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            // console.log(data)
            // console.log(data.data[0])
            //student primary key
            // console.log(data.data[0].id)
            //student name
            // console.log(data.data[0].name)
            if(data.data.length){
                for(var i=0;i<data.data.length;i++){
                    create_student_selection(data.data[i].id, data.data[i].name, data.data[i].roll, data.data[i].email)
                }
            }
        }
    })
  }

  //creation of options in select input
  function create_student_selection(student_pk, student_name){
    $('#select_student').append(
        `
        <option value="${student_pk}">${student_name}</option>
        `
    )
  }
//**** SELECT STUDENT DROPDOWN MENU ENDS****

//**** MARKS CRUD OPERATIONS STARTS HERE
var backup_pk_marks = -1
$('body').on('click','#save_changes',function(){
    if(backup_pk_marks==-1){
        $('#change_title_of_form').empty()
        $('#change_title_of_form').text("Create")
        create_marks()
    }
    else{
        $('#change_title_of_form').empty()
        $('#change_title_of_form').text("Update")
        update_marks_of_student()
    }
})
//create Marks
function create_marks(student_object){
    var maths = $('#maths').val()
    var physics = $('#physics').val()
    var chemistry = $('#chemistry').val()
    var english = $('#english').val()
    var hindi = $('#hindi').val()
    // var student = student_object
    var student= Number($('#select_student').val())
    var data={
        maths:maths,
        physics:physics,
        chemistry:chemistry,
        english:english,
        hindi:hindi,
        student:student,
        // student:{id:student},
    }
    fetch(
        MarksCRUD_API_url,{
            method:'POST',
            headers:{
                Accept:'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==201){
            get_marks_data()
            reset_form()
            backup_pk_marks = -1
            $('#change_title_of_form').empty()
            $('#change_title_of_form').text("Create")
            Swal.fire({
              position: "top-end",
              icon: "success",
              title: 'Marks Saved!!',
              showConfirmButton: false,
              timer: 1500
            });
        }
        else{
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: data.error,
                showConfirmButton: false,
                timer: 1500
              });
        }
    })
}
function change_title_of_the_form(){
    if(backup_pk_marks == -1){
        $('#change_title_of_form').text("Create")
    }
    else{
        $('#change_title_of_form').text("Update")
    }
}

//get marks all records from the database
function get_marks_data(){
    fetch(
        MarksCRUD_API_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken':getCookie("csrftoken"),
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            // console.log(data.data)
            // console.log(data.data[0])
            // console.log(data.data[0].student)
            $('#marks_table').empty()
            for(var i=0;i<data.data.length;i++){
                // console.log(data.data[i])
                var marks_id = data.data[i].id
                var student = data.data[i].student
                var maths = data.data[i].maths
                var physics = data.data[i].physics
                var chemistry = data.data[i].chemistry
                var english = data.data[i].english
                var hindi = data.data[i].hindi
                // console.log(marks_id)
                // console.log(student)
                // console.log(maths)
                // console.log(physics)
                // console.log(chemistry)
                // console.log(english)
                // console.log(hindi)
                create_marks_table(i,marks_id,student,maths,physics,chemistry,english,hindi)
            }
        }
        else{
            var i = ""
            var marks_id = "NULL"
            var student = "NULL"
            var maths = "NULL"

            var physics = "NULL"
            var chemistry = "NULL"
            var english = "NULL"
            var hindi = "NULL"
            $('#marks_table').empty()
            create_marks_table(i,marks_id,student,maths,physics,chemistry,english,hindi)
        }
    })
}

//Create Marks Table
function create_marks_table(i,marks_id,student,maths,physics,chemistry,english,hindi){
    $('#marks_table').append(
        `
        <tr>
            <th scope="row">${i+1}</th>
            <th scope="row" style="display:none">${marks_id}</th>
            <th scope="row" style="display:none">${student.id}</th>
            <td scope="row" style="display:none">${student}</td>
            <td scope="row" >${student.name}</td>
            <td>${maths}</td>
            <td>${physics}</td>
            <td>${chemistry}</td>
            <td>${english}</td>
            <td>${hindi}</td>
            <td>
                <div id="action_button_${marks_id}">
                    <button class="btn btn-dark" onclick="action_button('action_button_${marks_id}','${marks_id}','${student.id}','${student}','${maths}','${physics}','${chemistry}','${english}','${hindi}')">...</button>
                </div>
            </td>
        </tr>
        `
    )
}
function action_button(action_button_id,marks_id,student_id,student,maths,physics,chemistry,english,hindi){
    $(`#${action_button_id}`).empty()
    $(`#${action_button_id}`).append(
    `
    <button class="btn btn-primary" onclick="populate_marks_form('${marks_id}','${student_id}','${student}','${maths}','${physics}','${chemistry}','${english}','${hindi}')"><i class="fa-solid fa-pen"></i></button>
    <button class="btn btn-danger" onclick="delete_marks('${marks_id}')"><i class="fa-solid fa-trash"></i></button>    
    `
    )
}
//update marks
var student_id_backup = -1
var student_backup = []
function populate_marks_form(marks_id,student_id,student,maths,physics,chemistry,english,hindi){
    backup_pk_marks = marks_id
    student_id_backup = student_id
    student_backup.push(student)
    $('#change_title_of_form').empty()
    $('#change_title_of_form').text("Update")
    $('#maths').val(maths)
    $('#physics').val(physics)
    $('#chemistry').val(chemistry)
    $('#english').val(english)
    $('#hindi').val(hindi)
    $('#select_student').val(student_id)
}
//reset form 
function reset_form(){
    backup_pk_marks = -1
    student_id_backup = -1
    student_backup.length = 0
    $('#change_title_of_form').empty()
    $('#change_title_of_form').text("Update")
    $('#maths').val("")
    $('#physics').val("")
    $('#chemistry').val("")
    $('#english').val("")
    $('#hindi').val("")
    $('#select_student').val("-1")
}

//get data from the form of marks and update marks
function update_marks_of_student(){
    var maths= $('#maths').val()
    var physics= $('#physics').val()
    var chemistry= $('#chemistry').val()
    var english= $('#english').val()
    var hindi= $('#hindi').val()
    var select_student= $('#select_student').val()
    var id = backup_pk_marks
    var data = {
        id:id,
        student_id:student_id_backup,
        maths:maths,
        physics:physics,
        chemistry:chemistry,
        english:english,
        hindi:hindi,
        select_student:select_student,
    }
    fetch(
        MarksCRUD_API_url,{
            method:'PUT',
            headers:{
                Accept:'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            get_marks_data()
            reset_form()
            $('#change_title_of_form').empty()
            $('#change_title_of_form').text("Create")
            Swal.fire({
              position: "top-end",
              icon: "success",
              title: 'Marks Saved!!',
              showConfirmButton: false,
              timer: 1500
            });
        }
        else{
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: data.error,
                showConfirmButton: false,
                timer: 1500
              });
        }
    })
}
//delete marks of student
function delete_marks(marks_id){
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
            var data={
                marks_id:marks_id,
            }
            fetch(
                MarksCRUD_API_url,{
                    method:'DELETE',
                    headers:{
                        Accept:'application/json',
                        'Content-Type':'application/json',
                        'X-CSRFToken':getCookie("csrftoken"),
                    },
                    body:JSON.stringify(data)
                }
            ).then(response=>response.json())
            .then(data=>{
                if(data.status==200){
                    get_marks_data()
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: 'Marks Deleted!!',
                        showConfirmButton: false,
                        timer: 1500
                      });
                }
                else{
                    Swal.fire({
                        position: "top-end",
                        icon: "error",
                        title: data.error,
                        showConfirmButton: false,
                        timer: 1500
                      });
                }
            })
            get_marks_data()
        //   Swal.fire({
        //     title: "Deleted!",
        //     text: "Your file has been deleted.",
        //     icon: "success"
        //   });
        }
      });
}
//get one record
$('body').ready(function(){
    getOneRecordFromDB()
})
function getOneRecordFromDB() {
    marks_id=14
    fetch(`/marks/MarksCRUD_API/${marks_id}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);  // Handle the data here, such as updating UI
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
//**** MARKS CRUD OPERATIONS STARTS HERE
