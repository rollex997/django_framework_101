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
    get_category_data()

    $('#change_title_of_form').text("")
    $('#change_title_of_form').text("Create")    
})
var student_category_id_backup = -1
$('body').on('click','#save_changes',function(){
    if(student_category_id_backup==-1){
        get_category_data()
        create_student_category()
    }
    else{
        get_category_data()
        update_student_category()
    }
})
function create_student_category(){
    category = $('#category').val()
    var data={
        category:category,
    }
    fetch(
        StudentCategoryAPI_url,{
            method:'POST',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==201){
            //refresh the table 
            get_category_data()
            reset()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: 'Student Category Created!!',
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
function get_category_data(){
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
            // console.log(data.data[0])
            //id --> category id
            // console.log(data.data[0].id)
            //category name
            // console.log(data.data[0].category)
            $('#student_category_table').empty()
            for(var i=0;i<data.data.length;i++){
                create_table(i,data.data[i].id,data.data[i].category)
            }
        }
        else{

        }
    })
}
function create_table(i,category_id,category_name){
    $('#student_category_table').append(
        `
        <tr>
            <th scope="row">${i+1}</th>
            <th scope="row" style="display:none">${category_id}</th>
            <td>${category_name}</td>
            <td>
                <div id="action_button_${category_id}">
                    <button class="btn btn-dark" style="background:#EFBC9B;" onclick="action_button('action_button_${category_id}','${category_id}','${category_name}')">...</button>
                </div>
            </td>
        </tr>
        `
    )
}
function action_button(action_button_id,category_id,category_name){
    $(`#${action_button_id}`).empty()
    $(`#${action_button_id}`).append(
        `
           <button class="btn btn-primary" onclick="populate_student_category_form('${category_id}','${category_name}')"><i class="fa-solid fa-pen"></i></button>
           <button class="btn btn-danger" onclick="delete_student_category('${category_id}')"><i class="fa-solid fa-trash"></i></button>   
        `
    )
}
function populate_student_category_form(category_id,category_name){
    student_category_id_backup=category_id
    $('#category').val(`${category_name}`)
    $('#change_title_of_form').text("")
    $('#change_title_of_form').text("Update") 
}
function update_student_category(){
    var caregory_name = $('#category').val()
    // console.log(student_category_id_backup)
    var data={
        category_id:student_category_id_backup,
        category:caregory_name,
    }
    fetch(
        StudentCategoryAPI_url,{
            method:'PUT',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken"),
            },
            body:JSON.stringify(data)
    }).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            //refresh the table 
            get_category_data()
            student_category_id_backup=-1
            reset()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: 'Student Category Update!!',
                showConfirmButton: false,
                timer: 1500
              });
        }
        else{
            reset()
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
function reset(){
    student_category_id_backup=-1;
    $('#category').val("")
    $('#change_title_of_form').text("")
    $('#change_title_of_form').text("Create") 
}
function delete_student_category(category_id){
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
            id:category_id,
          }
          fetch(
            StudentCategoryAPI_url,{
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
                get_category_data()
              reset()
              student_category_id_backup=-1;
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