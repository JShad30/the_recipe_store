$(document).ready(function() {
	//The following allow the user to switch between the most popular and most recently uploaded post it notes on the home page
    $("#most-popular-button").on("click", function() {
		$("#most-popular-post-it-notes").toggle();
		$("#most-recent-post-it-notes").toggle();
	});
	$("#most-recent-button").on("click", function() {
	    $("#most-recent-post-it-notes").toggle();
	    $("#most-popular-post-it-notes").toggle();
	});
	
	//This section is for the meal type, preference and allergen cards on the home page, allowing the user to switch between them
	$("#meal-type-to-preference-button").on("click", function() {
		$("#meal-type-homepage-section").toggle();
		$("#preference-homepage-section").toggle();
	});
	$("#meal-type-to-allergen-button").on("click", function() {
		$("#meal-type-homepage-section").toggle();
		$("#allergen-homepage-section").toggle();
	});
	$("#preference-to-meal-type-button").on("click", function() {
		$("#meal-type-homepage-section").toggle();
		$("#preference-homepage-section").toggle();
	});
	$("#preference-to-allergen-button").on("click", function() {
	    $("#preference-homepage-section").toggle();
		$("#allergen-homepage-section").toggle();
	});
	$("#allergen-to-meal-type-button").on("click", function() {
	    $("#meal-type-homepage-section").toggle();
		$("#allergen-homepage-section").toggle();
	});
	$("#allergen-to-preference-button").on("click", function() {
	    $("#preference-homepage-section").toggle();
		$("#allergen-homepage-section").toggle();
	});
});