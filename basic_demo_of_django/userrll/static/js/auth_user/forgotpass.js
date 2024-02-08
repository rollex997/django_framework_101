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
    var pass1 = $('#pass1').val()
    var pass2 = $('#pass2').val()
    validate(pass1,pass2)
})
function validate(pass1,pass2){
    if(pass1==""||pass2==""){
        alert("fileds can't be empty")
    }
    else if(pass1!=pass2){
        alert("password do not match")
    }
    else{
        email_verification(pass1)
    }
}
function email_verification(pass1){
    var data={
        pass:pass1
    }
   fetch(
    verifyOTP_url,{
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
        window.location.href=verify_email
    }
   })
}
