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
    getCars()
})

function show_car(car_data_object){
    // console.log(car_data_object)
    $('#carsList').append(
        `
           <div class="col-lg-6 col-md-6">
                        <div class="car-box-3">
                            <div class="car-thumbnail">
                                <a onclick="open_car_detail(${car_data_object.id})" class="car-img">
                                    
                                    <div class="price-box">
                                        <span>$${car_data_object.price}</span>
                                    </div>
                                    <img class="d-block w-100" style = "height:262px" src="${car_data_object.car_photo}" alt="car">
                                </a>
                                
                            </div>
                            <div class="detail">
                                <h1 class="title">
                                    <a onclick="open_car_detail(${car_data_object.id})">${car_data_object.car_title}</a>
                                </h1>
                                <div class="location">
                                    <a onclick="open_car_detail(${car_data_object.id})">
                                        <i class="flaticon-pin"></i>${car_data_object.state}, ${car_data_object.city},
                                    </a>
                                </div>
                                <ul class="facilities-list clearfix">
                                    <li>${car_data_object.fuel_type}</li>
                                    <li>${car_data_object.miles} miles</li>
                                    <li>${car_data_object.transmission}</li>
                                    <li>${car_data_object.body_style}</li>
                                    <li>${car_data_object.color}</li>
                                    <li>${car_data_object.year}</li>
                                </ul>
                            </div>
                        </div>
                    </div>
        `
    )
}
function getCars(){
    fetch(
        cars_url,{
            method:'GET',
        }
    ).then(response=>response.json())
    .then(data=>{
        console.log(data)
        // console.log(data.results.data)
        // console.log(data.results.data[0])
        // //first get all the features names here
        // console.log(feature_names_holder);
        // console.log(data.next)
        if (data.next){
            // open_next(data.next)
            $('#temp_data_next').text(`${data.next}`);
        }
        if(data.previous){
            $('#temp_data_previous').text(`${data.previous}`);
        }
        $('#carsList').empty()
        for(var i=0;i<data.results.data.length;i++){
            show_car(data.results.data[i])
        }
    })
}
function getNextCars(nextURL){
    fetch(
        nextURL,{
            method:'GET',
        }
    ).then(response=>response.json())
    .then(data=>{
        console.log(data)
        // console.log(data.results.data)
        // console.log(data.results.data[0])
        // //first get all the features names here
        // console.log(feature_names_holder);
        // console.log(data.next)
        if (data.next){
            // open_next(data.next)
            $('#temp_data_next').text(`${data.next}`);
        }
        if(data.previous){
            $('#temp_data_previous').text(`${data.previous}`);
        }
        $('#carsList').empty()
        for(var i=0;i<data.results.data.length;i++){
            show_car(data.results.data[i])
        }
    })
}
function getPreviousCars(previousURL){
    fetch(
        previousURL,{
            method:'GET',
        }
    ).then(response=>response.json())
    .then(data=>{
        console.log(data)
        // console.log(data.results.data)
        // console.log(data.results.data[0])
        // //first get all the features names here
        // console.log(feature_names_holder);
        // console.log(data.next)
        if (data.next){
            // open_next(data.next)
            $('#temp_data_next').text(`${data.next}`);
        }
        if(data.previous){
            $('#temp_data_previous').text(`${data.previous}`);
        }
        $('#carsList').empty()
        for(var i=0;i<data.results.data.length;i++){
            show_car(data.results.data[i])
        }
    })
}
function open_car_detail(id){
    window.location.href=`car_details/${id}`
    // window.location.href=`cars/car_details/${id}`
}
$('body').on('click','#next_btn',function(){
        // getCars(next)
        console.log("next")
        open_next()
})

$('body').on('click','#previous_btn',function(){
        // getCars(previous)
        
        console.log("previous")
        open_previous()
})
function open_previous(){
    var textContent = $('#temp_data_previous').text();
        // getCars(pagination)
if (textContent.trim() !== '')
    {
        console.log(`previous : ${textContent}`)
        getPreviousCars(textContent)
    }
    else{
        console.log("previous is null")
    }
}
function open_next(){
    var textContent = $('#temp_data_next').text();
    // getCars(pagination)
    if (textContent.trim() !== '')
    {
        console.log(`next : ${textContent}`)
        getNextCars(textContent)
    }
    else{
        console.log("next is null")
    }
}