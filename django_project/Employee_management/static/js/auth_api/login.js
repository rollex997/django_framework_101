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
$('body').on('click','#login',function(){
    var username = $('#username').val();
    var password = $('#password').val();
    validate(username,password);
})
function validate(username,password){
 if (username==""||password==""){
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "fields can't be empty!",
      });
 }
 else{
    var data={
        username:username,
        password:password
    }
    login_function(data)
 }
}
function login_function(data){
    fetch(
        loginUser,{
            method:'POST',
            credentials:'same-origin',
            headers:{
                "X-Requested-With":'XMLHttpRequest',
                "X-CSRFToken":getCookie("csrftoken")
            },
            body:JSON.stringify({payload:data})
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            window.location.href=homepage
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Something went wrong try again",
              });
        }
    })
}
// forgetPasswordPage/<username>
$('body').on('click','#reset_password_btn',function(){
  var username = $('#username').val();
  validate_username(username)
})
function validate_username(username){
  if (username==""){
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "username is empty!",
    });
  }
  else{
    reset_password_fun(username)
  }
}
function reset_password_fun(username){
  window.location.href=`forgetPasswordPage/${username}`;
}