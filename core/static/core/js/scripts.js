/*(function ($) {
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
}*/

// this script is for my exp resume part 


secondPsychoArrow = document.getElementById('cat9')
secondPsychoArrow.style.display = 'none'
//*** VARIABLES ***
let hint = document.getElementById("hint")

//*** CALCULS   ***
const GetTriangle = function(elem){
    return elem.nextElementSibling.children[0]
}

const GetNumberVisibleChildren = function(paragraphe){
    count = 0
    for (child of paragraphe.children){
        if (child.className.search("visible") != -1){
            count ++ 
        }
    }
    return count
}
//*** FUNCTIONS ***
    const DisplayHide = (input, localStorClass, hintId, exampleId) =>{
        //value in local storage
        input.classList.add('bg-primary')
        if (localStorage.getItem(localStorClass)!== null){
            //remove visible element
            elemsToHide = Array.from(document.getElementsByClassName(localStorage.getItem(localStorClass)))
            elemsToHide.forEach(
                (elem) => {elem.classList.toggle("visible")}
                )
            btn_colored = document.getElementById(localStorage.getItem(localStorClass))
            btn_colored.classList.remove('bg-primary')
            if (localStorage.getItem(localStorClass) !== input.id){
                elemsToDisplay = Array.from(document.getElementsByClassName(input.id))
                elemsToDisplay.forEach(
                    (elem) => {elem.classList.toggle("visible")}
                )
                localStorage.removeItem(localStorClass)
                localStorage.setItem(localStorClass, input.id);
                return
            }
                localStorage.removeItem(localStorClass)
                console.log('--1--')
                document.getElementById(hintId).classList.toggle("visible")
                document.getElementById(exampleId).classList.toggle("visible")

        }else{
            elemsToDisplay = Array.from(document.getElementsByClassName(input.id))
            elemsToDisplay.forEach(
                (elem) => {elem.classList.toggle("visible")}
            )
            localStorage.setItem(localStorClass, input.id); 
            console.log('--2--' + exampleId)
            document.getElementById(hintId).classList.toggle("visible")
            document.getElementById(exampleId).classList.toggle("visible")

        }
    }

//display description when user clicks on btn for exp and educ
    const displayDescription = function(){
        for (butt of document.getElementsByClassName('display-button')){
            // click on display_button to 
            butt.onclick = (elem) => { 
                
                if (elem.target.className.search("arrow") == -1){
                    hintId = "hint-exp"  
                    exampleId = "example-exp"
                DisplayHide(elem.target, "exp-visible", hintId, exampleId)
                }else{
                    hintId = "hint-educ" 
                    exampleId = "example-educ"
                    DisplayHide(elem.target, "educ-visible", hintId, exampleId)
                }  
            }
        }
    }
    //click on title to display description
    for (title of document.getElementsByClassName('first-line')){
        title.onclick = function(e){
            let paragraphe = document.getElementById("paragraphe-exp")
            
            if (e.target.tagName == "A"){
                return
            }
            if (paragraphe.id == "paragraphe-educ"){
                return
            }
            console.log('>>>')
            console.log(e.target.className)
            if(e.target.className.search("exp") != -1){
                elem = e.target
            }else if (e.target.className.search("container-triangle") != -1){
                elem = e.target.previousElementSibling
            }else{
                elem = e.target.parentElement.previousElementSibling
            }
            console.log(elem)
            let description = elem.parentElement.parentElement.parentElement.nextElementSibling
            centerParagraphe    =   paragraphe.offsetTop + (paragraphe.offsetHeight/2)
            titlePosition    =   elem.offsetTop
            needToScrollDown = centerParagraphe - titlePosition
            let triangle = GetTriangle(elem)
            if (description.className.search("description") != -1){
                description.classList.toggle("hidden");
                triangle.classList.toggle('triangle-up')
                if (needToScrollDown < 40){
                    paragraphe.scrollBy(0, paragraphe.offsetHeight/2)
                }else{
                    paragraphe.scrollBy(0, 0 - paragraphe.offsetHeight/2 + 20)

                }
            }
        }
    }
// }
//myskill part 
    let paragrapheSkill = document.getElementById("paragraphe-skill")
    if (paragrapheSkill){
        heightParagrapheSkill = paragrapheSkill.offsetHeight
        console.log('paragrapheSkill:', paragrapheSkill)
        let radius = heightParagrapheSkill / 3.2; // adjust to move out skills in and out 
        let fields = $('.skill'),
          container = $('#container-skill'),
          width = container.width(),
          height = container.height();
        let angle = 0,
          step = (2 * Math.PI) / fields.length;
        fields.each(function() {
          var x = Math.round(width / 2 + radius * Math.cos(angle) - $(this).width() / 2);
          var y = Math.round(height / 2 + radius * Math.sin(angle) - $(this).height() / 2);
          if (window.console) {
            console.log($(this).text(), x, y);
          }
          $(this).css({
            left: x + 'px',
            top: y + 'px'
          });
          angle += step;
        });
    }
    

    containerSkill = document.getElementById("container-skill")

    for (element of document.getElementsByClassName("skill")){
        element.onclick = function(e){
            console.log("***")
            console.log("id = " + e.target.id)
            console.log("ls = ")
            console.log(localStorage)
            if (localStorage.getItem("skill-visible")!== null){
                console.log('Cet item est visible')
                console.log(localStorage.getItem("skill-visible"))
                idElemToHide = "desc-" + localStorage.getItem("skill-visible")
                elemToHide = document.getElementById(idElemToHide)
                elemToHide.classList.toggle('visible')
                console.log('Cet item a été effacé')
                if (localStorage.getItem("skill-visible") !== e.target.id){
                    description = document.getElementById("desc-" + e.target.id)
                    description.classList.toggle('visible')
                    localStorage.clear()
                    localStorage.setItem("skill-visible", e.target.id);
                    console.log('Cet item est visible')
                    console.log(localStorage.getItem("skill-visible"))
                    return
                }
                    localStorage.clear()
                    containerSkill.classList.toggle('centered-skill-circle')
            }else{
                description = document.getElementById("desc-" + e.target.id)
                description.classList.toggle('visible')
                localStorage.setItem("skill-visible", e.target.id);
                containerSkill.classList.toggle('centered-skill-circle')
            }
        }
    }

//success part
    navSuccess = document.getElementById('nav-success')
    allSuccessLi = document.getElementsByClassName("li-success")
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms))
    }
    const elems = Array.from(document.getElementsByClassName('checkbox'))
    elems.reverse()
    const checkTheBox = elem => {
      return sleep(200).then(v => {
        elem.parentElement.classList.toggle('opacity-0')
        elem.checked = true
        if (elem.id == 'ch1'){
            return sleep(800).then(v =>{
                elem.checked = false
                elem.parentElement.classList.toggle('bg-primary')
            })
        }
      })
    }

    const forLoop = async _ => {
      for (let index = 0; index < elems.length; index++) {
        const elem = elems[index]
        const checkedBox = await checkTheBox(elem)
      }
    }

    firstLi = allSuccessLi[0]
    if (firstLi.firstElementChild.checked != false){
        firstLi.firstElementChild.checked = false
        }

    let topOfWindow = $("#success").offset().top;
    visible = false
    $(".main-part").scroll(function () {
        // console.log($(".main-part"))
        var successPart = $("#success").offset().top;
        calc = parseFloat(100 - (successPart/topOfWindow) * 100).toFixed(0)
        // console.log( calc, '%')
        if (calc >= 95){
            console.log(visible)
            if (visible == false){
                console.log('trigger now !! ')
                forLoop()
                visible = true
            }
        }
    });
    navSuccess.onclick = () => {
        // document.getElementById('checkbox-container').classList.toggle('visible')
        forLoop()
        visible = true
    }
const main = function(){
    localStorage.clear()
    console.log(localStorage)
    displayDescription()
}
main()

    // $(document).ready(function(){
    //     // hide all experiences
    //     $('.resume-section-content').hide();
    //     // show class experiences
    //     const dico = {professorat: ".prof", animation: ".anim", 
    //     direction: ".dir", autres: ".aut"}; 
    //     $(".togg").click(function(){ 
    //         const txtButton = $(this).text()
            
    //         $(dico[txtButton]).toggle(1000);
    //         if ($(this).css("background-color") =="rgb(202, 125, 96)"){
    //             $(this).css("background-color", "rgb(128, 51, 0)");
    //             $(this).css("font-weight","bold");
    //         }else{
    //             $(this).css("background-color", "rgb(202, 125, 96)");
    //             $(this).css("font-weight","normal");
    //         }  
    //         $([document.documentElement, document.body]).animate({
    //             scrollTop: $("#experience").offset().top
    //             }, 2000);          
    //     });
        // ****

    // });
// })(jQuery); // End of use strict
