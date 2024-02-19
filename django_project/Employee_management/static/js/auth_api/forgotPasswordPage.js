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
$('body').on('click','#submit',function(){
    var password = $('#password').val()
    var password2 = $('#password2').val()
    validate(password,password2)
})
function validate(password,password2){
    if (password=="" || password2==""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "fields can't be empty!",
          });
    }
    else if(password != password2){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "password don't watch",
          });
    }
    else{
        var data = {
            password:password
        }
        get_password(data)
    }
}
function get_password(data){
    fetch(
        verifyOTPForgotPassword,{
            method:'POST',
            credentials:'same-origin',
            headers:{
                "X-Requested-With":"XMLHttpRequest",
                "X-CSRFToken":getCookie("csrftoken")
            },
            body:JSON.stringify({payload:data})
        }
    ).then(response=>response.json())
    .then (data=>{
        if (data.status==200){
            window.location.href=verify_email
        }
    })
}