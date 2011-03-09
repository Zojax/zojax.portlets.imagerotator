/* zojax image rotator portlet */
$(document).ready(function() {

$('.imagerotator-container').each(function() {
//Set Default State of each banners piece
var $this = $(this);
var play;
if ($this.find('.buttons').length)
    $('.thumbs').empty();
$this.find(".thumbs").show();
$this.find(".thumbs a:first").addClass("active");

//Get size of images, how many there are, then determin the size of the image reel.
var imageWidth = $this.find(".banner").width();
var imageSum = $this.find(".imagereel img").size();
var imageReelWidth = imageWidth * imageSum;

//Adjust the image reel to its new size
$this.find(".imagereel").css({'width' : imageReelWidth});

//thumbs + Slider Function
var rotate = function($active){
    var triggerID = parseInt($active.attr("rel")) - 1; //Get number of times to slide
    var image_reelPosition = triggerID * imageWidth; //Determines the distance the image reel needs to slide
    
    $this.find(".thumbs a").removeClass('active'); //Remove all active class
    $active.addClass('active'); //Add active class (the $active is declared in the rotateSwitch function)
    
    //Slider Animation
    $this.find(".imagereel").css({
    left: -image_reelPosition
    });
    //Теxt Animation
    $this.find(".textreel").css({
    left: -image_reelPosition
    });

};

//Rotation + Timing Event
var rotateSwitch = function($active){
    play = setInterval(function(){ //Set timer - this will repeat itself every 3 seconds
    if (!$active)
        $active = $this.find('.thumbs a.active');
    else
        $active = $active.next();
    if ( $active.length === 0) { //If paging reaches the end...
        $active = $this.find('.thumbs a:first'); //go back to first
    }
    rotate($active); //Trigger the paging and slider function
    }, 5000); //Timer speed in milliseconds
};

rotateSwitch(); //Run function on launch

//On Hover
$this.find(".imagereel a").hover(function() {
        clearInterval(play); //Stop the rotation
    }, function() {
        rotateSwitch(); //Resume rotation
    });

//On Click
$this.find(".thumbs a").click(function() {
        var $active = $(this); //Activate the clicked thumbs
        //Reset Timer
        clearInterval(play); //Stop the rotation
        rotate($active); //Trigger rotation immediately
        rotateSwitch($active); // Resume rotation
        return false; //Prevent browser jump to link anchor
        });
    });
});