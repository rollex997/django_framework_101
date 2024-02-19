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
$('body').on('click','#register',function(){
    var username = $('#username').val();
    var email = $('#email').val();
    var phone = $('#phone').val();
    var password1 = $('#password1').val();
    var password2 = $('#password2').val();
    validation(username,email,phone,password1,password2)
})
function validation(username,email,phone,password1,password2){
    if(username == "" || email == "" || phone == "" || password1 == "" || password2==""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Input can't be empty!",
          });
    }
    else if(password1!=password2){
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Password don't match!",
          });
    }
    else{
        var data={
            username:username,
            email:email,
            phone:phone,
            password1:password1,
            password2:password2,
        }
        get_data(data)
    }
}
function get_data(data){
    fetch(
        registerUser,{
            method:'POST',
            credentials:'same-origin',
            headers:{
                "X-Requested-With":"XMLHttpRequest",
                "X-CSRFToken":getCookie("csrftoken")
            },
            body:JSON.stringify({'payload':data})
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            window.location.href=verifyOTPpage
        }
        else if(data.status==400){
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Something went wrong try again",
              });
        }
    })
}