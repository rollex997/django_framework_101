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
    username = $('#username').val()
    pass=$('#pass').val()
validate(username,pass)
})
function validate(username,pass){
    if (username==""||pass==""){
        alert("email or password is empty")
    }
    else{
            var data ={
                username:username,
                pass:pass
            }
            get_values(data)
    }
}
function get_values(data){
fetch (
    login_user_url,{
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
    console.log(data.status)
    if(data.status==200){
        window.location.href = main;
    }
    if(data.status==400){
        alert("Password or email not correct")
    }
})
}