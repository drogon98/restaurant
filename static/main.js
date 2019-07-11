var menu = document.querySelector(".menu-bar");

var links = document.querySelector(".nav-links");

var all_links = document.querySelectorAll('.link');


menu.addEventListener('click', function () {
    menu.classList.toggle('change');
    links.classList.toggle('show-menu');
})


var slideIndex = 0;

function showSlides() {
    var slides = document.getElementsByClassName('slide');

    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = "block";

    setTimeout(showSlides, 4000);
}

showSlides();

var revSlideIndex = 0;

function showRevSlides() {
    var rev_slides = document.getElementsByClassName('car-review');

    for (var i = 0; i < rev_slides.length; i++) {
        rev_slides[i].style.display = "none";
    }

    revSlideIndex++;

    if (revSlideIndex > rev_slides.length) {
        revSlideIndex = 1;
    }

    rev_slides[revSlideIndex - 1].style.display = "block";

    setTimeout(showRevSlides, 4000);
}

showRevSlides();