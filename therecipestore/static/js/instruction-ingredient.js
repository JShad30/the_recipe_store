//Adding ingredients and instructions when the buttons are pressed
$(document).ready(function() {
	
	var ingredientidnumber = 5;
	var instructionidnumber = 3;
	
	$("#add-ingredient-button").on("click", function() {
	    $(".ingredient-textboxes").append('<input class="create-recipe-ingredient" id="ingredients-' + ingredientidnumber + '" type="text" name="ingredients-' + ingredientidnumber + '" placeholder="Ingredient" value/>');
	    ingredientidnumber++;
	});
	
	$("#add-instruction-button").on("click", function() {
		$(".instruction-textboxes").append('<textarea class="create-recipe-instruction" id="instructions-' + instructionidnumber + '" placeholder="Instruction" name="instructions-' + instructionidnumber + '"></textarea>');
		instructionidnumber++;
	});
});