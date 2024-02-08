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
    otp = $('#otp').val()
    verify_otp(otp)
})
function verify_otp(otp){
    var data = {
        otp:otp
    }
    fetch(
        verify_email_otp_verify_url,{
            method:'POST',
            credentials:'same-origin',
            headers:{
                'X-Requested-With':'XMLHttpRequest',
                'X-CSRFToken':getCookie("csrftoken")
            },
            body: JSON.stringify({payload:data})
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            alert("email verified")
            window.location.href=login_url
        }
        else if (data.status==400){
            alert("otp did not matched")
        }
        else if (data.status==404){
            alert("error try again")
        }
        else if(data.status==402){
            console.log("user does not exist")
        }
    })
}