var ID=0;
$('body').ready(function(){
    console.log("enroll js is linked successfully");
    $(`#form_insert_data`).empty();
    $(`#show_data_table_container`).empty();
})
//insert data logic starts
$('body').on('click','#insert_data',function(){
    $(`#show_data_table_container`).empty();
    create_insert_data_form();
})
function create_insert_data_form(){
    $(`#form_insert_data`).empty();
    $(`#form_insert_data`).append(
        `
        <div class="row mb-3">
        <div class="col-sm-12 col-md-6 col-lg-4">
            <label for="name" class="form-label">Name</label>
            <input type="text" class="form-control" id="name">
        </div>
        <div class="col-sm-12 col-md-6 col-lg-4">
            <label for="mobile" class="form-label">Mobile Number</label>
            <input type="text" class="form-control" id="mobile">
        </div>
        <div class="col-sm-12 col-md-6 col-lg-4">
            <label for="city" class="form-label">City</label>
            <input type="text" class="form-control" id="city">
        </div>
        <div class="col-sm-12 col-md-6 col-lg-4">
            <label for="roll_no" class="form-label">Roll number</label>
            <input type="text" class="form-control" id="roll_no">
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-2 col-lg-2 mb-3">
            <button class="btn btn-primary" id="submit_button">Submit</button>
        </div>
        <div class="col-sm-12 col-md-2 col-lg-2 mb-3">
            <button class="btn btn-danger" id="cancel_button">Cancel</button>
        </div>
    </div>
        `
    )
    $(`#mobile_error`).addClass("display-none");
}
/* Submit button logic starts*/ 
$('body').on('click','#submit_button',function(){
    if(ID==0){
        insert_data();
        clear_input_fields();
    }
    else{
        edit_data();
        clear_input_fields();
    }
})
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
function insert_data(){
    var insert_url = insert_data_url;
    var data = {
        name : $(`#name`).val(),
        mobile : $(`#mobile`).val(),
        city : $(`#city`).val(),
        roll_no : parseInt($(`#roll_no`).val())
    }
        fetch(insert_url, {
            method: "POST",
            credentials: "same-origin",
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({payload: data})
          })
          .then(response => response.json())
          .then(data => {
            console.log(data);
          });    
}
/* Submit button logic ends*/ 

/* candel button logic starts */
$(`body`).on('click','#cancel_button', function(){
    clear_input_fields();
})
function clear_input_fields(){
    $(`#name`).val("");
    $(`#mobile`).val("");
    $(`#city`).val("");
    $(`#roll_no`).val("");
}
/* candel button logic ends */
//insert data logic ends

//Get data logic starts
$('body').on('click','#show_data', function(){
    $(`#form_insert_data`).empty();
    show_data_table();
})
function show_data_table(){
    $(`#show_data_table_container`).empty();
    $(`#show_data_table_container`).append(
        `
        <table class="table">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">SID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Mobile Number</th>
                    <th scope="col">City</th>
                    <th scope="col">Roll Number</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody id="data_table">
                </tbody>
              </table>
        `
    );
    get_data();
}
//get data using get method
function get_data(){
    url = get_data_url;
    fetch(url, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        }
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        console.log(data.context[0].name);
        console.log(data.context.length);
        data_backup = data;
        //data table starts
        var k=1;
        $(`#data_table`).empty()
        for ( var i = 0; i<data.context.length;i++){
            $(`#data_table`).append(`
            <tr>
                    <td>${k++}</td>
                    <td class="data_ID">${data.context[i].SID}</td>
                    <td class="name">${data.context[i].name}</td>
                    <td class="mobile">${data.context[i].mobile}</td>
                    <td class="city">${data.context[i].city}</td>
                    <td class="roll_number">${data.context[i].roll_number}</td>
                    <td><button class="btn btn-dark text-light" onclick="open_form('${data.context[i].SID}', 
                    '${data.context[i].name}', '${data.context[i].mobile}', '${data.context[i].city}',
                    '${data.context[i].roll_number}')"><i class="fa-solid fa-pen"></i></button>
                    <button class="btn btn-danger" onclick="data_delete('${data.context[i].SID}')"><i class="fa-solid fa-trash"></i></button>
                    </td>
                  </tr>       
            `)
        }
        //data table ends
      });
}
//Get data logic ends

//edit data logic starts
function open_form(SID, name, mobile, city, roll_number){
    ID = 0;
    $(`#show_data_table_container`).empty();
    create_insert_data_form();
    ID = Number(SID);
    console.log(`selected ID = ${ID}`);
    $(`#name`).val(name);
    $(`#mobile`).val(mobile);
    $(`#city`).val(city);
    $(`#roll_no`).val(roll_number);
}
function edit_data(){
        var data = {
            SID : ID,
            name : $(`#name`).val(),
            mobile : $(`#mobile`).val(),
            city : $(`#city`).val(),
            roll_no : parseInt($(`#roll_no`).val())
        }
        fetch(update_data_url, {
            method: "PUT",
            credentials: "same-origin",
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            body: JSON.stringify({payload: data})
          })
          .then(response => response.json())
          .then(data => {
            console.log(data);
          });
          ID = 0;
}
//edit data logic ends

//delete_data logic starts
function data_delete(ID){
    var data = {
        SID : ID
    }
    var choice = confirm("Are you sure you want to delete record?");
    if(choice==true){
        fetch(delete_data_url, {
            method: "PUT",
            credentials: "same-origin",
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            body: JSON.stringify({payload: data})
          })
          .then(response => response.json())
          .then(data => {
            console.log(data);
            show_data_table();
          });
          //refresh the table after deleting the record
    }
}
//delete_data logic ends