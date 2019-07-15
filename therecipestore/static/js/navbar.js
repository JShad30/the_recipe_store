var width = $(window).width(); // Setting the window of the screen as a variable

//Adding and removeing the classes
$(document).ready(function() {
    $("#navbar-dropdown").on("click", function() {
    	$(this).toggleClass("close");
		$(".navbar-links").slideToggle("fast");
	});
});

// Reset page when window size changes
$(window).resize(function() {
    location.reload(true)
});