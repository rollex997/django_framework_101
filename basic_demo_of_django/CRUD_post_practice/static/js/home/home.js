/* get csrf token from the cookies starts */
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
/* get csrf token from the cookies ends */

$('body').ready(function(){
    console.log("Home js was linked successfully!!");
    // Swal.fire("SweetAlert2 is working!");
    // Get the ID from the query parameter
    const urlParams = new URLSearchParams(window.location.search);
    const receivedID = urlParams.get('id');

    // Use the receivedID as needed
    get_data_by_ID(receivedID);
})
function get_data_by_ID(receivedID){
    if (receivedID){
        var ID_=receivedID;
        console.log(receivedID);
        var data = {
            ID : ID_
        }
        fetch(
            url,{
                method:'POST',
                credentials : 'same-origin',
                headers:{
                    'X-Requested-With' : 'XMLHttpRequest',
                    'X-CSRFToken' : getCookie('csrftoken')
                },
                body : JSON.stringify({payload : data}),
            }
        ).then(response=>response.json())
        .then(
            data=>{
                console.log(data)
                console.log(data.context.name);
                console.log(data.context.roll_no);
                console.log(data.context.mobile);
                console.log(data.context.father_name);
                console.log(data.context.mother_name);
                console.log(data.context.father_mobile);
                $('#data_field').append(`
                <p>${data.context.name}</p>
                <p>${data.context.roll_no}</p>
                <p>${data.context.mobile}</p>
                <p>${data.context.father_name}</p>
                <p>${data.context.mother_name}</p>
                <p>${data.context.father_mobile}</p>
            `);
            }
        )
    }
}