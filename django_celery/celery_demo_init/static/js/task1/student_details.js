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
    change_title_of_the_form()
    get_student_data()
})
function get_student_data(){
    fetch(
        StudentAPI_url,{
            method:'GET',
        headers:{
            Accept:'application/json'
        }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            // console.log(data)
            // console.log(data.data[0])
            $('#student_table').empty()
            for(var i=0;i<data.data.length;i++){
                // console.log(data.data[i])
                var id = data.data[i].id
                var name = data.data[i].name
                var roll = data.data[i].roll
                var email = data.data[i].email
                create_student_table(i,id,name,roll,email)
            }
            // console.log(row_button_cliacked_id)
        }
    })
} 
 function create_student_table(i,id,name,roll,email){
    $('#student_table').append(
        `
        <tr>
            <th scope="row">${i+1}</th>
            <th scope="row" style="display:none">${id}</th>
            <td>${name}</td>
            <td>${roll}</td>
            <td>${email}</td>
            <td>
                <div id="action_button_${id}">
                    <button class="btn btn-dark" onclick="action_button('action_button_${id}','${id}','${name}','${roll}','${email}')">...</button>
                </div>
            </td>
        </tr>
        `
    )
 }
 function action_button(action_button_id,id,name,roll,email){
  $(`#${action_button_id}`).empty()
  $(`#${action_button_id}`).append(
    `
    <button class="btn btn-primary" onclick="update_student_form('${id}','${name}','${roll}','${email}')"><i class="fa-solid fa-pen"></i></button>
    <button class="btn btn-danger" onclick="delete_student('${id}')"><i class="fa-solid fa-trash"></i></button>    
    `
  )
 }
 var record_id_backup = -1
 function change_title_of_the_form(){
  if(record_id_backup==-1){
    $('#change_title_of_form').empty()
    $('#change_title_of_form').text("Create")
  }
  else{
    $('#change_title_of_form').empty()
    $('#change_title_of_form').text("Update")
  }
 }
 function update_student_form(id,name,roll,email){
  record_id_backup = id
  $('#name').val(name)
  $('#roll').val(roll)
  $('#email').val(email)
  change_title_of_the_form()
 }
function reset_form(){
  $('#name').val("")
  $('#roll').val("")
  $('#email').val("")
}
$('body').on('click','#save_changes',function(){
  if(record_id_backup==-1){
    var name = $('#name').val()
      var roll = Number($('#roll').val())
      var email = $('#email').val()
      var data = {
        name:name,
        roll:roll,
        email:email
      }
    create_student(data)
  }
  else{
    update_student_data()
  }
})
 function update_student_data(){
  Swal.fire({
    title: "Do you want to save the changes?",
    showDenyButton: true,
    showCancelButton: true,
    confirmButtonText: "Save",
    denyButtonText: `Don't save`
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      var name = $('#name').val()
      var roll = $('#roll').val()
      var email = $('#email').val()
      var data = {
        id:record_id_backup,
        name:name,
        roll:roll,
        email:email
      }
      fetch(
        StudentAPI_url,{
          method:'PUT',
          headers:{
            'Accept':'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken"),
          },
          body: JSON.stringify(data)
        }
      ).then(response=>response.json())
      .then(data=>{
        if(data.status==200){
          get_student_data()
          reset_form()
          record_id_backup = -1
          change_title_of_the_form()
          Swal.fire({
            position: "top-end",
            icon: "success",
            title: 'Changes Saved!!',
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
    } else if (result.isDenied) {
      Swal.fire("Changes are not saved", "", "info");
    }
  });
 }
 function create_student(data){
  fetch(
    StudentAPI_url,{
      method:'POST',
      headers:{
        Accept:'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken':getCookie("csrftoken"),
      },
      body:JSON.stringify(data)
    }
  ).then(response=>response.json())
  .then(data=>{
    if(data.status==201){
      get_student_data()
      reset_form()
      record_id_backup = -1
      change_title_of_the_form()
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
 function delete_student(id){
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
      var data = {
        id:id,
      }
      fetch(
        StudentAPI_url,{
          method:'DELETE',
          headers:{
            Accept:'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken':getCookie("csrftoken"),
          },
          body:JSON.stringify(data)
        }
      ).then(response=>response.json())
      .then(data=>{
        if (data.status==200){
          get_student_data()
          reset_form()
          record_id_backup = -1
          change_title_of_the_form()
          Swal.fire({
            position: "top-end",
            icon: "success",
            title: 'Data Deleted',
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
  });
 }