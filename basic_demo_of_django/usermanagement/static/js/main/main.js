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
$('body').on('click','#logout',function(){
logout_user()
})
function logout_user(){
    console.log("logout")
    fetch(logout_url,{
        method:'POST',
        credentials:'same-origin',
        headers:{
            'X-Requested-With':'XMLHttpRequest',
            'X-CSRFtoken' : getCookie('csrftoken')
        }
    }).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            window.location.href=login_url
        }
    })
}
$('body').on('click','#change_pass',function(){
  var username = $('#username').text()
  if(username == ""){
      alert('Username empty')
  }
  else{
      window.location.href='auth/changePasswordPage' + `/${username}`
  }
})