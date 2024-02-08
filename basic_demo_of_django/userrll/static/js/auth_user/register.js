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
    username=$('#userName').val()
    email=$('#userEmail').val()
    pass1=$('#userPass1').val()
    pass2=$('#userPass2').val()
    validate(username,email,pass1,pass2)
})
function validate(username,email, pass1, pass2){
    if(username=="" || email=="" || pass1 =="" || pass2 ==""){
        alert("input can't be empty")
    }
    else{
        var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        var Eflag=0;
        if (pattern.test(email)) {
            Eflag=1
        } else {
            alert("Please enter a valid email address");
            Eflag=0
        }
        var Pflag=0
        if(pass1 == pass2){
            Pflag=1
        }
        else{
            alert("password don't match")
            Pflag=0
        }
        if (Eflag==1&&Pflag==1){
            var data = {
                username:username,
                email : email,
                password1 : pass1,
                password2 : pass2
            }
            get_form_val(data)
            send_form_data_email(data)
        }
    }
}
function get_form_val(data){
    url = register_url
    fetch(url,{
        method:'POST',
        credentials:'same-origin',
        headers:{
            "X-Requested-With":"XMLHttpRequest",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify({payload:data})
    }).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            alert("check your mail")
        }
        if(data.status==599){
            alert("user already exist")
        }
    })
}
function send_form_data_email(data){
    fetch(
        email_otp_url,{
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
        if (data.status==200){
            window.location.href=verifyotp_url
        }
    })
}