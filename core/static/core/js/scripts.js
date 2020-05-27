/*!
    * Start Bootstrap - Resume v6.0.0 (https://startbootstrap.com/template-overviews/resume)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-resume/blob/master/LICENSE)
    */
    (function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#sideNav",
    });
    
    $(document).ready(function(){
        // hide all experiences
        $('.resume-exp').hide();
        // show class experiences
        const dico = {professorat: ".prof", animation: ".anim", 
        direction: ".dir", autres: ".aut"}; 
        $(".togg").click(function(){ 
            const txtButton = $(this).text()
            
            $(dico[txtButton]).toggle(1000);
            console.log($(this).css("background-color"))   
            if ($(this).css("background-color") =="rgb(202, 125, 96)"){
                $(this).css("background-color", "rgb(128, 51, 0)");
                $(this).css("font-weight","bold");
            }else{
                $(this).css("background-color", "rgb(202, 125, 96)");
                $(this).css("font-weight","normal");
            }  
            $([document.documentElement, document.body]).animate({
                scrollTop: $("#experience").offset().top
                }, 2000);          
        });
        // ****
        $('.resume-educ').hide();
        $('.listing-project').hide();
        $(".opener").click(function(){
            $(".opener").toggle();
            $(this).toggle();
            //recup id
            const id = $(this).attr("id");
            //add id to resum-form
            const name_class = ".educ-"+id;
            //open resum-form-id 
            $(name_class).toggle(1000);
            $([document.documentElement, document.body]).animate({
                scrollTop: $("#formation").offset().top
                }, 2000);
        });
        $(".listing").click(function(){
            $(".listing-project").toggle(1000);
            $([document.documentElement, document.body]).animate({
                scrollTop: $("#formation").offset().top
                }, 2000);
        });
             
    });
})(jQuery); // End of use strict
