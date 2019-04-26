$(document).ready(function() {
	//When the search link type dropdown is selected, the search link will slide down
    $("#most-popular-button").on("click", function() {
		$("#most-popular-post-it-notes").toggle();
		$("#most-recent-post-it-notes").toggle();
	});
	$("#most-recent-button").on("click", function() {
	    $("#most-recent-post-it-notes").toggle();
	    $("#most-popular-post-it-notes").toggle();
	});
});