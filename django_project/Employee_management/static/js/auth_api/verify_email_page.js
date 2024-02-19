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
$('body').on('click','#verify',function(){
    var otp = $('#otp').val()
    validate(otp)
})
$('body').on('click','#verify',function(){
    var otp = $('#otp').val()
    validate(otp)
})
function validate(otp){
    if(otp==""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "otp field is empty!",
          });
    }
    else{
        var data={
            otp:otp
        }
        get_val(data)
    }
}
function get_val(data){
    fetch(
        verify_email_otp_verify,{
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
        if(data.status==200){
            window.location.href="login"
        }
    })
}