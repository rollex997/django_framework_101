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
 
$('body').ready(function(){
    console.log("this is homepage js")
    get_data()
})
function show_data(data,i){
    $('#show_data').append(
        `
        <p>name = ${data.name} , city =  ${data.city}</p>
        `
    )
}
function get_data(){
    fetch(home,{
        method:'POST',
        credentials:'same-origin',
        headers:{
            'X-Requested-With':'XMLHttpRequest',
            'X-CSRFToken':getCookie('csrftoken')
        }
    }).then(response=>response.json())
    .then(data=>{
        $('#show_data').empty()
        for (var i=0;i<data.context.length;i++){
            show_data(data.context[i],i)
        }
    })
}