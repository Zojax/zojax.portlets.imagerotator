/* zojax image rotator portlet */
$(document).ready(function() {
$(".buttons-block").hide();

$('.imagerotator-container').each(function() {
//Set Default State of each banners piece
var $this = $(this);
var play;
var first = $this.find("..banner-item.first");
first.siblings().find('.item-text').css({opacity:0});
first.siblings().find('.item-image').css({opacity:0});
first.removeClass('first');
$this.find(".thumbs").show();
if ($this.find('.buttons').length)
    $('.thumbs').css('display', 'none');

//thumbs + Slider Function
var rotate = function($active){
    var triggerID = parseInt($active.attr("rel")) - 1; //Get number of times to slide
    var $current = $(".banners li").eq(triggerID);
    $this.find(".thumbs a").removeClass('active'); //Remove all active class
    $active.addClass('active'); //Add active class (the $active is declared in the rotateSwitch function)
    
    //Slider Animation
    $this.find('.item-text').animate({opacity:0}, {queue: false, duration: 2000});
    $current.siblings().find('.item-image').animate({opacity:0}, {queue: false, duration: 2000});
    $current.find('.item-image').animate({opacity:1}, {queue: false, duration: 2000});
    $current.find('.item-text').delay(2000).animate({opacity:1});

};

//Rotation + Timing Event
var rotateSwitch = function($active){
    play = setInterval(function(){ //Set timer - this will repeat itself every 3 seconds
    if (!$active)
        $active = $this.find('.thumbs a.active');
    $active = $active.next();
    if ( $active.length === 0) { //If paging reaches the end...
        $active = $this.find('.thumbs a:first'); //go back to first
    }
    rotate($active); //Trigger the paging and slider function
    }, 5000); //Timer speed in milliseconds
};

rotateSwitch(); //Run function on launch

//On Hover
$this.find(".imagereel a").hover(
    function() {
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

    $this.find(".buttons ul li").hover(
	    function() {
          $(this).find('.buttons-item').hide();
          $(this).find(".buttons-block").slideToggle("slow");
        }, function() {
          $(this).find(".buttons-block").stop();
          $this.find(".buttons-block").hide();
          $this.find(".buttons-item").show();
      });

    });
});