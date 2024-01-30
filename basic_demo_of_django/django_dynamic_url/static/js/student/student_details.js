var data_ ;
$('body').ready(function(){
    var data = {
        student_name:$('#student_name').text(),
    Maths : $(`#Maths`).text(),
    Physics : $(`#Physics`).text(),
    Chemistry : $(`#Chemistry`).text(),
    Computer : $(`#Computer`).text(),
    English : $(`#English`).text(),
    Total_marks_obtained : $(`#Total_marks_obtained`).text(),
    Total_Marks : $(`#Total_Marks`).text(),
    Percentage : $(`#Percentage`).text(),
    passing_percentage : $(`#passing_percentage`).text(),
    pass_fail : $(`#pass_fail`).text(),
    }
    data_  = data
})
function create_marks_card(marks){
    var icon = `<i class="fa-solid fa-xmark text-danger"></i>`;
    if(marks.pass_fail == "True"){
        icon = `<i class="fa-solid fa-check text-success"></i>`;
    }
    else{
        icon = `<i class="fa-solid fa-xmark text-danger"></i>`;
    }
    $('#marks_card').append(
        `
        <div class="card-deck">
        <div class="card mb-4" style="width: 22rem;">
            <div class="card-body">
              <h5 class="card-title">${marks.student_name}'s Marks</h5>
              <h6 class="card-subtitle mb-2 text-muted">Marks Detail</h6>
              <div class="row">
                <p class="card-text">Maths : ${marks.Maths}</p>
            </div>
            <div class="row">
                <p class="card-text">Physics : ${marks.Physics}</p>
            </div>
            <div class="row">
                <p class="card-text">Chemistry : ${marks.Chemistry}</p>
            </div>
            <div class="row">
                <p class="card-text">Computer : ${marks.Computer}</p>
            </div>
            <div class="row">
                <p class="card-text">English : ${marks.English}</p>
            </div>
            <div class="row">
                <p class="card-text">Hindi : ${marks.English}</p>
            </div>
            <div class="row">
                <p class="card-text">Total_marks_obtained : ${marks.Total_marks_obtained}</p>
            </div>
            <div class="row">
                <p class="card-text">Total_Marks : ${marks.Total_Marks}</p>
            </div>
            <div class="row">
                <p class="card-text">Percentage : ${marks.Percentage}</p>
            </div>
            <div class="row">
                <p class="card-text">passing_percentage : ${marks.passing_percentage}</p>
            </div>
            <div class="row">
                <p class="card-text">Pass : ${icon}</p>
            </div>
              <a href="#" class="btn btn-primary my-1" id="hide_marks">Hide</a>
            </div>
          </div>
    </div>
        `
    )
}
$('body').on('click','#show_marks',function(){
    show_marks();
})
function show_marks(){
    if (data_.Maths == "" && data_.Physics == "" && data_.Chemistry == "" && data_.Computer == "" && data_.English == "" && data_.Total_marks_obtained == "" && data_.Total_Marks == "" && data_.Percentage == "" && data_.passing_percentage == "" && data_.pass_fail == ""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Marks does not exist!"
          });
    }
    else{
        create_marks_card(data_)
    }
}
$('body').on('click','#hide_marks',function(){
    $('#marks_card').empty()
    $('#marks_card').empty()
})