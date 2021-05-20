document.addEventListener('DOMContentLoaded', () =>
{
showSlides(slideIndex = 1)
}) 
    
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    slides[i].style.opacity = "0"; 
}
  slides[slideIndex-1].style.display = "block";
  slides[slideIndex-1].style.opacity = "1";
  slides[slideIndex-1].style.transition ="all 1s";
  
}
