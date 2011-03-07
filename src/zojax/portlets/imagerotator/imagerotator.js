/* zojax image rotator portlet */
$(document).ready(function() {

//Set Default State of each banners piece
$(".thumbs").show();
$(".thumbs a:first").addClass("active");

//Get size of images, how many there are, then determin the size of the image reel.
var imageWidth = $(".banner").width();
var imageSum = $(".imagereel img").size();
var imageReelWidth = imageWidth * imageSum;

//Adjust the image reel to its new size
$(".imagereel").css({'width' : imageReelWidth});

//thumbs + Slider Function
rotate = function(){
var triggerID = $active.attr("rel") - 1; //Get number of times to slide
var image_reelPosition = triggerID * imageWidth; //Determines the distance the image reel needs to slide

$(".thumbs a").removeClass('active'); //Remove all active class
$active.addClass('active'); //Add active class (the $active is declared in the rotateSwitch function)

//Slider Animation
$(".imagereel").animate({
left: -image_reelPosition
}, 500 );
//Теxt Animation
$(".textreel").animate({
left: -image_reelPosition
}, 500 );

};

//Rotation + Timing Event
rotateSwitch = function(){
play = setInterval(function(){ //Set timer - this will repeat itself every 3 seconds
$active = $('.thumbs a.active').next();
if ( $active.length === 0) { //If paging reaches the end...
$active = $('.thumbs a:first'); //go back to first
}
rotate(); //Trigger the paging and slider function
}, 5000); //Timer speed in milliseconds
};

rotateSwitch(); //Run function on launch

//On Hover
$(".imagereel a").hover(function() {
clearInterval(play); //Stop the rotation
}, function() {
rotateSwitch(); //Resume rotation
});

//On Click
$(".thumbs a").click(function() {
$active = $(this); //Activate the clicked thumbs
//Reset Timer
clearInterval(play); //Stop the rotation
rotate(); //Trigger rotation immediately
rotateSwitch(); // Resume rotation
return false; //Prevent browser jump to link anchor
});

});