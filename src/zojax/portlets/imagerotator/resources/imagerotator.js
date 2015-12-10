/* zojax image rotator portlet */
$(document).ready(function() {

$.preLoadImages = function(imageList,callback) {
  var pic = [], i, total, loaded = 0;
  if (typeof imageList != 'undefined') {
    if ($.isArray(imageList)) {
      total = imageList.length; // used later
      for (i=0; i < total; i++) {
        pic[i] = new Image();
        pic[i].onload = function() {
          this.onload = function() {return false};
          loaded++; // should never hit a race condition due to JS's non-threaded nature
          if (loaded == total) {
            if ($.isFunction(callback)) {
              callback();
            }
          }
        };
        pic[i].src = imageList[i];
        if (pic[i].complete || (jQuery.browser.msie && parseInt(jQuery.browser.version) == 6))
            pic[i].onload()
      }
    }
    else {
      pic[0] = new Image();
      pic[0].onload = function() {
        this.onload = function() {return false};
        if ($.isFunction(callback)) {
          callback();
        }
      }
      pic[0].src = imageList;
      if (pic[0].complete || (jQuery.browser.msie && parseInt(jQuery.browser.version) == 6))
          pic[0].onload()
    }
  }
  pic = undefined;
};

var toPreload=[];
$(".banners").find("img").each(function(){
  toPreload.push($(this).attr("src"));
});

$.preLoadImages(toPreload,function(){
    $('.preloader').remove();
  }
);

$(".buttons-block").hide();

$('.imagerotator-container').each(function() {
//Set Default State of each banners piece
var $this = $(this);
var play;
var first = $this.find(".banner-item.first");
first.css({'z-index' : '70'});
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
    $this.find('.item-text').animate({opacity:0}, {queue: false, duration: 1000});
	$current.siblings().css({'z-index' : '69'});
    $current.siblings().find('.item-image').animate({opacity:0}, {queue: false, duration: 1000});
    $current.find('.item-image').animate({opacity:1}, {queue: false, duration: 1000});
	$current.css({'z-index' : '70'});
    $current.find('.item-text').delay(1000).animate({opacity:1});

};

//Rotation + Timing Event
var rotateSwitch = function($active){
    if ($this.find('.item-image').length < 2)
        return;
    play = setInterval(function(){ //Set timer - this will repeat itself every 3 seconds
    if (!$active)
        $active = $this.find('.thumbs a.active');
    $active = $active.next();
    if ( $active.length === 0) { //If paging reaches the end...
        $active = $this.find('.thumbs a:first'); //go back to first
    }
    rotate($active); //Trigger the paging and slider function
    }, 6500); //Timer speed in milliseconds
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
    var iconhover = function() {
        var $active = $(this); //Activate the clicked thumbs
        //Reset Timer
        clearInterval(play); //Stop the rotation
        rotate($active); //Trigger rotation immediately
        return false; //Prevent browser jump to link anchor
        };
    $this.find(".thumbs a").click(iconhover).hover(iconhover, function(){
        var $active = $(this); //Activate the clicked thumbs
        //Reset Timer
        rotateSwitch($active); // Resume rotation
        return false; //Prevent browser jump to link anchor
        });

    $this.find(".buttons ul li").hover(
	    function() {
          $(this).find('.buttons-item').hide();
          $(this).find(".buttons-block").css({height:'auto'});
          $(this).find(".buttons-block").stop().css({display:'block'}).animate({ height: $(this).find(".buttons-block").height() }, 1000);

	    }, function() {
	      var $li = $(this);
	      $(this).find(".buttons-block").stop().slideUp("fast", function(){$li.find('.buttons-item').show()});
	 });

    $this.find(".buttons ul li .button-item").click(function() {
        $(this).find('.buttons-item').hide();
        $(this).find(".buttons-block").css({height:'auto'});
        $(this).find(".buttons-block").show();
        //return false;
        });

    });
});