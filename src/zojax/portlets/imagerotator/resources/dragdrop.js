$(document).ready(function() {

    // Sort
    $(".form-widgets-images .multi-widget").children().each(function(index) {
        if ($(this).attr('id') == 'form-widgets-images-'+index+'-row') {
            $('#form-widgets-images-'+index+'-widgets-position').val(index);
        }
    });

    $(".form-widgets-buttons .multi-widget").children().each(function(index) {
        if ($(this).attr('id') == 'form-widgets-buttons-'+index+'-row') {
            $('#form-widgets-buttons-'+index+'-widgets-position').val(index);
        }
    });

    $( ".form-widgets-images .multi-widget" ).sortable({
        connectWith: ".form-widgets-images .multi-widget",
        axis: "y",
        update: function(event, ui) {
            parent = ui.item.parent();
            parent.children().each(function(index) {
                var Id = $(this).attr('id');
                Id = Id.replace('form-widgets-images-', '');
                Id = Id.replace('-row', '');
                $('#form-widgets-images-'+Id+'-widgets-position').val(index);
            });
        }
    }).disableSelection();

    $( ".form-widgets-buttons .multi-widget" ).sortable({
        connectWith: ".form-widgets-buttons .multi-widget",
        axis: "y",
        update: function(event, ui) {
            parent = ui.item.parent();
            parent.children().each(function(index) {
                var Id = $(this).attr('id');
                Id = Id.replace('form-widgets-buttons-', '');
                Id = Id.replace('-row', '');
                $('#form-widgets-buttons-'+Id+'-widgets-position').val(index);
            });
        }
    }).disableSelection();

    // Expand-collapse
    $(".form-widgets-images .multi-widget .row > div.widget").hide();
    $(".form-widgets-buttons .multi-widget .row > div.widget").hide();

    $(".form-widgets-images .multi-widget .row > div.label").addClass("closed");
    $(".form-widgets-buttons .multi-widget .row > div.label").addClass("closed");

    var toggleItem = function() {
        var $glideElement = $(this);
	    if ($glideElement.next().is(":hidden")) {
		    // show it
		    $glideElement.removeClass("closed");
		    $glideElement.addClass("open");
		    $glideElement.next().slideDown();
	    } else {
		    // hidde it
		    $glideElement.removeClass("open");
		    $glideElement.addClass("closed");
		    $glideElement.next().slideUp();
	    }
	    return false;
    }

    $(".form-widgets-images .multi-widget .row > div.label").click(toggleItem);
    $(".form-widgets-buttons .multi-widget .row > div.label").click(toggleItem);
});
