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
$(document).ready(function() {
    // Your JavaScript code here
    $('#home_view').css('display', 'block')
    $('#employee_view').hide()
});

$('body').on('click','#employee',function(){
    employee()
})
function employee(){
    $('#home_view').hide()
    $('#employee_view').css('display', 'block')
    get_emp_data()
    display_table()
}
$('body').on('click','#home',function(){
    home()
})
function home(){
    console.log("home")
    $('#home_view').css('display', 'block')
    $('#employee_view').hide()
}

//IO logic starts here
var flag=0;
$('body').on('click','#save',function(){
    var company_name = $('#company_name').val();
    var role = $('#role').val();
    var date_of_joining = $('#date_of_joining').val();
    var last_date = $('#last_date').val();
    if(flag==0){
        validate_form(company_name,role,date_of_joining,last_date)
    }
    else if(flag==2){
        edit_data(company_name,role,date_of_joining,last_date)
    }
})
function validate_form(company_name,role,date_of_joining,last_date){
    if (company_name=="" || role=="" || date_of_joining=="" || last_date==""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "fields can't be empty!",
          });
    }
    else{
        var data={
            company_name:company_name,
            role:role,
            date_of_joining:date_of_joining,
            last_date:last_date
        }
        post_employee(data)
    }
}
function post_employee(data){
    fetch(
        empWorkCreate,{
            method:'POST',
            credentials:'same-origin',
            headers:{
            "X-Requested-With":"XMLHttpRequest",
            "X-CSRFToken":getCookie("csrftoken")
            },
            body:JSON.stringify({payload:data})
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==201){
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "Your work has been saved",
                showConfirmButton: false,
                timer: 1500
              });
              reset_form();
              $('#table_body').empty();
              get_emp_data();
              flag=1;
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Could not add Employee experience!",
              });
        }
    })
}
function display_table(i,ID,company_name,date_of_joining,last_date,role){
    $('#table_body').append(
        `
        <tr>
        <td scope="col">${i}</td>
        <td scope="row" style="display:none">${ID}</td>
        <td>${company_name}</td>
        <td>${role}</td>
        <td>${date_of_joining}</td>
        <td>${last_date}</td>
        <td>
        <button class="btn btn-dark" onclick="set_form('${ID}','${company_name}','${role}','${date_of_joining}','${last_date}')"><i class="fa-solid fa-pen"></i></button>
        <button class="btn btn-danger" onclick="delete_emp('${ID}')"><i class="fa-solid fa-trash"></i></button>
        </td>
        </tr>
        `
    )
}

function get_emp_data() {
    fetch(
        empWorkRead, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                "X-Requested-With": "XMLHttpRequest", // Correct spelling
                "X-CSRFToken": getCookie("csrftoken")
            }
        }
    ).then(response => response.json())
    .then(data => {
        $('#table_body').empty();
        console.log(data.context[0]);
        for (var i=0;i<data.context.length;i++){
            display_table(i,data.context[i].ID,data.context[i].company_name,data.context[i].date_of_joining,data.context[i].last_date,data.context[i].role)
        }
    });
}
var ID_;
$('body').on('click','#cancel',function(){
    reset_form()
    flag=0
})
function reset_form(){
    $('#company_name').val("");
    $('#role').val("");
    $('#date_of_joining').val("");
    $('#last_date').val("");
}
function set_form(ID, company_name, role, date_of_joining, last_date) {
    ID_=ID;
    $('#company_name').val(company_name);
    $('#role').val(role);
    $('#date_of_joining').val(date_of_joining);
    $('#last_date').val(last_date);
    flag=2;
}
function edit_data(company_name,role,date_of_joining,last_date){
    var data ={
        ID:ID_,company_name:company_name,role:role,date_of_joining:date_of_joining,last_date:last_date
    }
    Swal.fire({
        title: "Do you want to save the changes?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Save",
        denyButtonText: `Don't save`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          fetch(
            empEdit,{
                method:'POST',
                credentials:'same-origin',
                headers:{
                    'X-Requested-With':'XMLHttpRequest',
                    'X-CSRFToken':getCookie("csrftoken")
                },
                body:JSON.stringify({payload:data})
            }
        ).then(response=>response.json())
        .then(data=>{
            if(data.status==200){
                Swal.fire("Saved!", "", "success");
                $('#table_body').empty();
                get_emp_data();
                reset_form();
            }
            else{
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "Could not update Employee experience!",
                  });
            }
        })
        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
}

function delete_emp(ID){
    var data={
        ID:ID
    }
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
            fetch(
                empdelete,{
                    method:'POST',
                    credentials:'same-origin',
                    headers:{
                        "X-Requested-With":"XMLHttpRequest",
                        "X-CSRFToken":getCookie("csrftoken")
                    },
                    body:JSON.stringify({payload:data})
                }
            ).then(response=>response.json())
            .then(data=>{
                if (data.status==200){
                    $('#table_body').empty();
                    get_emp_data();
                    Swal.fire({
                        title: "Deleted!",
                        text: "Your file has been deleted.",
                        icon: "success"
                      });
                }
                else{
                    Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: "Could not delete Employee experience!",
                      });
                }
            })
        }
      });
}
//IO logic ends here