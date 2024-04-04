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
    get_all_student_categories()
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
                // var category=data.data[i].category[0]
                // // console.log(name)
                // console.log(category)
                var category = data.data[i].category[0];  // Assuming data is the response object
                if(category){
                  var categoryId = category.id;  // Accessing the id property
                  var categoryName = category.category;  // Accessing the category property
  
                  // console.log("Category ID:", categoryId);
                  // console.log("Category Name:", categoryName);
                  create_student_table(i,id,name,roll,email,categoryId,categoryName)
                }
                else{
                  var categoryId = null
                  var categoryName = null
                  create_student_table(i,id,name,roll,email,categoryId,categoryName)
                }
            }
            // console.log(row_button_cliacked_id)
        }
    })
} 
 function create_student_table(i,id,name,roll,email,categoryId,categoryName){
    $('#student_table').append(
        `
        <tr>
            <th scope="row">${i+1}</th>
            <th scope="row" style="display:none">${id}</th>
            <th scope="row" style="display:none">${categoryId}</th>
            <td>${name}</td>
            <td>${roll}</td>
            <td>${email}</td>
            <td>${categoryName}</td>
            <td>
                <div id="action_button_${id}">
                    <button class="btn btn-dark" onclick="action_button('action_button_${id}','${id}','${name}','${roll}','${email}','${categoryId}','${categoryName}')">...</button>
                </div>
            </td>
        </tr>
        `
    )
 }
 function action_button(action_button_id,id,name,roll,email,categoryId,categoryName){
  $(`#${action_button_id}`).empty()
  $(`#${action_button_id}`).append(
    `
    <button class="btn btn-primary" onclick="update_student_form('${id}','${name}','${roll}','${email}','${categoryId}','${categoryName}')"><i class="fa-solid fa-pen"></i></button>
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
 function update_student_form(id,name,roll,email,categoryId,categoryName){
  record_id_backup = id
  $('#name').val(name)
  $('#roll').val(roll)
  $('#email').val(email)
  if (categoryId){
    $('#select_student').val(categoryId)
  }
  else{
    $('#select_student').val("-1")
  }
  change_title_of_the_form()
 }
function reset_form(){
  $('#name').val("")
  $('#roll').val("")
  $('#email').val("")
  $('#select_student').val("-1")
}
$('body').on('click','#save_changes',function(){
  if(record_id_backup==-1){
    var name = $('#name').val()
      var roll = Number($('#roll').val())
      var email = $('#email').val()
      var student_category = [Number($('#select_student').val())]
      console.log(student_category)
      var data = {
        name:name,
        roll:roll,
        email:email,
        category:student_category,
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
      var student_category = [Number($('#select_student').val())]
      var data = {
        id:record_id_backup,
        name:name,
        roll:roll,
        email:email,
        category:student_category,
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
      $('#name').val("")
      $('#roll').val("")
      $('#email').val("")
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
 //get one student record starts
 $('body').ready(function(){
  getOneRecordFromDB()
 })
function getOneRecordFromDB() {
  student_id=8
    fetch(`/StudentAPI/${student_id}/`, {
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
        // console.log(data);  // Handle the data here, such as updating UI
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
//get one student ends

//student category
//get all student category
function get_all_student_categories(){
  fetch(
    StudentCategoryAPI_url,{
      method:'GET',
      headers:{
        Accept:'application/json',
        'Content-Type':'application/json',
      }
    }
  ).then(response=>response.json())
  .then(data=>{
    if(data.status==200){
      //id
      // console.log(data.data[0].id)
      // var id = data.data[0].id
      //category
      // console.log(data.data[0].category)
      // var category = data.data[0].category
      $('#select_student').empty()
      $('#select_student').append(
        `
        <option value="-1">::SELECT STUDENT CATEGORY::</option>
        `
    )
      for(var i=0;i<data.data.length;i++){
        var id = data.data[i].id
        var category = data.data[i].category
        create_student_category_selection(id, category)
      }
    }
    else{
      $('#select_student').append(
        `
        <option value="-1">::SELECT STUDENT CATEGORY::</option>
        `
    )
    }
  })
}
  //creation of options in select input
  function create_student_category_selection(category_pk, student_category){
    $('#select_student').append(
        `
        <option value="${category_pk}">${student_category}</option>
        `
    )
  }