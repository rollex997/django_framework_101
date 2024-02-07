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
$('body').on('click','#change_pass',function(){
    var pass1 = $('#pass1').val()
    var pass2 = $('#pass2').val()
    var passOLD = $('#passOLD').val()
    Validite(pass1,pass2,passOLD)
})
function Validite(pass1,pass2,passOLD){
    if(pass1==""||pass2==""||passOLD==""){
        alert("password is empty")
    }
    else{
        if(pass1==pass2){
            change_pass(pass1,pass2,passOLD)
        }
        else{
            alert("password don't match")
        }
    }
}
function change_pass(pass1,pass2,passOLD){
    var data={
        username:$('#username').text(),
        pass1:pass1,
        pass2:pass2,
        passOLD:passOLD
    } 
    console.log(data)
    fetch(changePassword_url,{
        method:'POST',
        credentials:'same-origin',
        headers:{
            'X-Requested-With':'XMLHttpRequest',
            'X-CSRFToken':getCookie("csrftoken")
        },
        body:JSON.stringify({'payload':data})
    }).then(response=>response.json())
    .then(data=>{
        console.log(data)
        if(data.status==200){
            alert("password change successfully!!!");
            window.location.href=login_url
        }
        else if(data.status==404){
            alter("user not found")
        }
    })
}