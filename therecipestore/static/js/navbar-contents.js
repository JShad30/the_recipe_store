//Adding and removing the classes
$(document).ready(function() {
	//When the search link type dropdown is selected, the search link will slide down
    $("#search-link").on("click", function() {
		$("#search-link-dropdown").slideToggle("fast");
		if($(window).width() >= 768) {
			$("#meal-type-dropdown").slideUp("fast");
			$("#allergens-dropdown").slideUp("fast");
		}
	});

	//If the mouse leaves the search dropdown in larger screen views, then the dropdown menu will scroll up
	$("#search-link-dropdown").mouseleave(function() {
		$("#search-link-dropdown").slideUp("fast");
	});
	

	//When the meal type dropdown is selected, the menu will slide down
	$("#meal-type").on("click", function() {
		$("#meal-type-dropdown").slideToggle("fast");
		if($(window).width() >= 768) {
			$("#search-link-dropdown").slideUp("fast");
			$("#allergens-dropdown").slideUp("fast");
		}
	});

	//If the mouse leaves the meal type dropdown in larger screen views, then the menu will scroll up
	$("#meal-type-dropdown").mouseleave(function() {
		$("#meal-type-dropdown").slideUp("fast");
	});

	//When the allergens dropdown is selected, the menu will slide down
	$("#allergens").on("click", function() {
		$("#allergens-dropdown").slideToggle("fast");
		if($(window).width() >= 768) {
			$("#meal-type-dropdown").slideUp("fast");
			$("#search-link-dropdown").slideUp("fast");
		}
	});

	//If the mouse leaves the allergens dropdown in larger screen views, then the menu will scroll up
	$("#allergens-dropdown").mouseleave(function() {
		$("#allergens-dropdown").slideUp("fast");
	});
});

// Reset page when window size changes
//$(window).resize(function() {
    //location.reload(true)
//});