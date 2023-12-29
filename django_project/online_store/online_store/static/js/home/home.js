console.log("home.js is successfully linked to the home page ")


//handling nav bar starts
//Imports related to nav bar starts--->
//Theme related settings in jquery
var nav_bar_option_underline_color = "black";
var nav_bar_option_underline_height = "10%";
var nav_bar_option_underline_width = "100%";

//import nav bar option items
var home = $("#home");
var Admin=$("#Admin");
var about_us = $("#About_us");
var contact_us = $("#Contact_us");
var my_cart = $("#My_cart");
//selecting underline in the nav menu items elements
var underline_home = $("#home .underline_nav");
var underline_Admin = $("#Admin .underline_nav");
var underline_About_us = $("#About_us .underline_nav");
var underline_Contact_us = $("#Contact_us .underline_nav");
var underline_My_cart = $("#My_cart .underline_nav");
//Imports related to nav bar ends--->

$(document).on('DOMContentLoaded', function(){
    nav_bar_on_mouse_hover_style();
    nav_bar_defaults_on_page_load();
});

//this function will load the nav bar items default style
function nav_bar_defaults_on_page_load(){
    console.log("nav_bar_defaults_on_page_load function called");
    //nav bar items default style configuration
    home.on( "mouseleave", function(){
        underline_home.css("height", nav_bar_option_underline_height);
        underline_home.css("width", "0%");
        //theme nav bar color
        underline_home.css("background-color", "transparent");
        underline_home.css("transition", "1s");
    } );
    Admin.on( "mouseleave", function(){
        underline_Admin.css("height", nav_bar_option_underline_height);
        underline_Admin.css("width", "0%");
        //theme nav bar color
        underline_Admin.css("background-color", "transparent");
        underline_Admin.css("transition", "1s");
    } );
    about_us.on( "mouseleave", function(){
        underline_About_us.css("height", nav_bar_option_underline_height);
        underline_About_us.css("width", "0%");
        //theme nav bar color
        underline_About_us.css("background-color", "transparent");
        underline_About_us.css("transition", "1s");
    } );
    contact_us.on( "mouseleave", function(){
        underline_Contact_us.css("height", nav_bar_option_underline_height);
        underline_Contact_us.css("width", "0%");
        //theme nav bar color
        underline_Contact_us.css("background-color", "transparent");
        underline_Contact_us.css("transition", "1s");
    } );
    my_cart.on( "mouseleave", function() {
        underline_My_cart.css("height", nav_bar_option_underline_height);
        underline_My_cart.css("width", "0%");
        //theme nav bar color
        underline_My_cart.css("background-color", "transparent");
        underline_My_cart.css("transition", "1s");
    });
}

//this function will change the nav bar items style on mouse hover
function nav_bar_on_mouse_hover_style(){
    console.log("nav_bar_on_mouse_hover_style function called");

    //apply css on nav bar option itmes on mouse hover
    home.on( "mouseenter", function(){
        underline_home.css("height", nav_bar_option_underline_height);
        underline_home.css("width", nav_bar_option_underline_width);
        //theme nav bar color
        underline_home.css("background-color", nav_bar_option_underline_color);
        underline_home.css("transition", "1s");
    } );
    Admin.on( "mouseenter", function(){
        underline_Admin.css("height", nav_bar_option_underline_height);
        underline_Admin.css("width", nav_bar_option_underline_width);
        //theme nav bar color
        underline_Admin.css("background-color", nav_bar_option_underline_color);
        underline_Admin.css("transition", "1s");
    } );
    about_us.on( "mouseenter", function(){
        underline_About_us.css("height", nav_bar_option_underline_height);
        underline_About_us.css("width", nav_bar_option_underline_width);
        //theme nav bar color
        underline_About_us.css("background-color", nav_bar_option_underline_color);
        underline_About_us.css("transition", "1s");
    } );
    contact_us.on( "mouseenter", function(){
        underline_Contact_us.css("height", nav_bar_option_underline_height);
        underline_Contact_us.css("width", nav_bar_option_underline_width);
        //theme nav bar color
        underline_Contact_us.css("background-color", nav_bar_option_underline_color);
        underline_Contact_us.css("transition", "1s");
    } );
    my_cart.on( "mouseenter", function(){
        underline_My_cart.css("height", nav_bar_option_underline_height);
        underline_My_cart.css("width", nav_bar_option_underline_width);
        //theme nav bar color
        underline_My_cart.css("background-color", nav_bar_option_underline_color);
        underline_My_cart.css("transition", "1s");
    } );

    //apply css on mouse leave nav bar option items
    home.on( "mouseleave", function(){
        underline_home.css("height", nav_bar_option_underline_height);
        underline_home.css("width", "0%");
        //theme nav bar color
        underline_home.css("background-color", "transparent");
        underline_home.css("transition", "1s");
    } );
    Admin.on( "mouseleave", function(){
        underline_Admin.css("height", nav_bar_option_underline_height);
        underline_Admin.css("width", "0%");
        //theme nav bar color
        underline_Admin.css("background-color", "transparent");
        underline_Admin.css("transition", "1s");
    } );
    about_us.on( "mouseleave", function(){
        underline_About_us.css("height", nav_bar_option_underline_height);
        underline_About_us.css("width", "0%");
        //theme nav bar color
        underline_About_us.css("background-color", "transparent");
        underline_About_us.css("transition", "1s");
    } );
    contact_us.on( "mouseleave", function(){
        underline_Contact_us.css("height", nav_bar_option_underline_height);
        underline_Contact_us.css("width", "0%");
        //theme nav bar color
        underline_Contact_us.css("background-color", "transparent");
        underline_Contact_us.css("transition", "1s");
    } );
    my_cart.on( "mouseleave", function() {
        underline_My_cart.css("height", nav_bar_option_underline_height);
        underline_My_cart.css("width", "0%");
        //theme nav bar color
        underline_My_cart.css("background-color", "transparent");
        underline_My_cart.css("transition", "1s");
    });
    
}

//handling nav bar ends