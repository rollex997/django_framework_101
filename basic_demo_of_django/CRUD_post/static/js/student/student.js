var ID=0;
$('body').ready(function(){
    console.log("students js is linked successfully");
    get_data();
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

//create Table 
function CreateTable(data, i){
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
                  <button class="btn btn-dark mb-1" onclick="update_form('${data.context[i].student_ID}', '${data.context[i].name}', '${data.context[i].roll_no}', '${data.context[i].mobile}', '${data.context[i].father_name}', '${data.context[i].mother_name}', '${data.context[i].father_mobile}')"><i class="fa-solid fa-pen"></i></button>
                  <button class="btn btn-danger mb-1" onclick="delete_data('${data.context[i].student_ID}')"><i class="fa-solid fa-trash"></i></button>
                </td>
              </tr>
    `)
}

/* reset form starts */
function reset_form(){
    $('#name').val("");
    $('#roll_no').val("");
    $('#mobile').val("");
    $('#father_name').val("");
    $('#mother_name').val("");
    $('#father_mobile').val("");
}
$('body').on('click','#cancel_button',function(){
    reset_form();
})
/* reset form ends */

/*using post method send data from HTML to Backend */
  $('body').on('click','#submit_button',function(){
    if(ID==0){
        if($('#name').val()=="" || $('#roll_no').val()=="" || $('#mobile').val()=="" || $('#father_name').val()=="" || $('#mother_name').val()=="" || $('#father_mobile').val()=="")
        {
            alert("input fields can not be empty");
        }
        else{
            post_data();
        }
    }
    else{
        update_data();
        
    }
    reset_form();
})
function post_data(){
    var insert_url = insert_data_url;
    var data = new Object();
    data.name = $('#name').val();
    data.roll_no = $('#roll_no').val();
    data.mobile = $('#mobile').val();
    data.father_name = $('#father_name').val();
    data.mother_name = $('#mother_name').val();
    data.father_mobile = $('#father_mobile').val();
        fetch(insert_url, {
            method : "POST",
            credentials : "same-origin",
            headers:{
                "X-Requested-With" : "XMLHttpRequest",
                "X-CSRFToken" : getCookie("csrftoken"),
            },
            body : JSON.stringify({payload: data})
        })
        .then(
            response => response.json()
        )
        .then(
            data => {
                console.log(data);
                get_data();
            }
        );
}
/*using post method send data from HTML to Backend */

/*using post method Get data from backend */
function get_data(){
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
            console.log(` get data function was called`);
            console.log(data);
            for( var i=0;i<data.context.length;i++){
                CreateTable(data, i);
            }
        }
    );
}
/*using post method Get data from backend */

/* using post method to update data */
function update_form(student_ID, name, roll_no, mobile, father_name, mother_name, father_mobile){
    ID = 0;
    ID = Number(student_ID);
    console.log(`Selected ID = ${ID}`);
    $('#name').val(name);
    $('#roll_no').val(roll_no);
    $('#mobile').val(mobile);
    $('#father_name').val(father_name);
    $('#mother_name').val(mother_name);
    $('#father_mobile').val(father_mobile);
}
function update_data(){
    var update_url = update_data_url;
    if($('#name').val()=="" || $('#roll_no').val()=="" || $('#mobile').val()=="" || $('#father_name').val()=="" || $('#mother_name').val()=="" || $('#father_mobile').val()=="")
    {
        alert("input fields can not be empty");
    }
    else{
        var data = {
            student_ID : ID,
            name : $('#name').val(),
            roll_no : $('#roll_no').val(),
            mobile : $('#mobile').val(),
            father_name : $('#father_name').val(),
            mother_name : $('#mother_name').val(),
            father_mobile : $('#father_mobile').val(),
        }
        fetch(update_url,
            {
                method : "POST",
                credentials : "same-origin",
                headers:{
                    "X-Requested-With" : "XMLHttpRequest",
                    "X-CSRFToken" : getCookie("csrftoken"),
                },
                body: JSON.stringify({payload : data})
            }
            )
            .then(response => response.json())
            .then(data => {
                console.log(data);
                get_data();
                ID=0;
            });
    }
        
}
/* using post method to update data */

/* delete_data starts */
function delete_data(ID){
    var data = {
        student_ID : ID
    }
    var choice = confirm("are you sure you want to delete this record?");
    if(choice==true){
        fetch(delete_data_url,{
            method:"POST",
            credentials : "same-origin",
            headers : {
                "X-Requested-With" : "XMLHttpRequest",
                "X-CSRFToken" : getCookie("csrftoken"),
            },
            body: JSON.stringify({payload : data})
        })
        .then(
            response => response.json()
        )
        .then(
            data =>{
                console.log(data);
                get_data();
                ID=0;
            }
        );
    }
}
/* delete_data ends */