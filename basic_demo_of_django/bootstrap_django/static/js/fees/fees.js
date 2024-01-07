console.log("fees js is linked successfully")
$(document).on('click', '#submit', function(){
    var selected = $('#select').val();
    var textbox = $('#select_option_value')
    textbox.val(selected);
  })










$(document).ready(function(){
    get_value();
})
function csrfSafeMethod(method) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function get_value() {
    var selector = $('#fees_options');
    // $.ajaxSetup({
    //     beforeSend: function (xhr, settings) {
    //         // if not safe, set csrftoken
    //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //         }
    //     }
    // });
    $.ajax({
        url: "{% url 'fees_api' %}",  // URL mapped to your Django view
        type: "GET",
        dataType: "json",

        success: function (data) {
            // Handle the retrieved data
            console.log(data);

            // Clear existing options
            selector.empty();

            // Append new options based on the data
            $.each(data.data, function (key, value) {
                selector.append('<option value="' + value + '">' + key + '</option>');
            });
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}