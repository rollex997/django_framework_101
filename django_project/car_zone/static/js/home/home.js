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
// get_team_members_data()
})
//js is not working for this particullar theme 
// card is lost when window is resized
function team_members_list(data){
    $('#team_items_list').append(
        `
        <div class="slick-slide-item">
          <div class="team-1">
            <div class="photo">
              <a href="#">
                <img
                  src="/media/${data.photo}"
                  alt="team-1"
                  class="img-fluid"
                />
              </a>
              <div class="social-list clearfix">
                <a href="{% url '${data.facebook_link}' %}" class="facebook-bg"
                  ><i class="fa fa-facebook"></i
                ></a>
                <a href="{% url '${data.facebook_link}' %}" class="twitter-bg"><i class="fa fa-twitter"></i></a>
              </div>
            </div>
            <div class="details">
              <h4><a href="team-detail.html">${data.firstname} ${data.lastname}</a></h4>
              <h5>${data.designation}</h5>
            </div>
          </div>
        </div>
        `
    )
}
function get_team_members_data(){
  fetch(
    GetTeamMembers,{
      method:'GET',
      credentials:'same-origin',
      headers:{
        'X-RequestedWith':'XMLHttpRequest',
        'X-CSRFToken':getCookie("csrftoken")
      }
    }
  ).then(response=>response.json())
  .then(data=>{
    console.log(data)
    $('#team_items_list').empty()
    for(var i = 0;i<data.context.length;i++){
      team_members_list(data.context[i])
    }
  })
}