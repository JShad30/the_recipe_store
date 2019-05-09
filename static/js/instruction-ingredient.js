//Adding ingredients and instructions when the buttons are pressed
$(document).ready(function() {
    $("#add-ingredient-button").on("click", function() {
        $(".ingredient-textboxes").append('<input class="create-recipe-ingredient" type="text" name="ingredient" placeholder="Ingredient"/>');
	});
	$("#add-instruction-button").on("click", function() {
	    $(".instruction-textboxes").append('<textarea class="create-recipe-instruction" placeholder="Instruction"/></textarea>');
	});
});