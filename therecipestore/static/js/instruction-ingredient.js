// Adding ingredients and instructions when the buttons are pressed
$(document).ready(function() {
	
	// Variables set to a number one higher than the number of preset ingredients/ instruction textboxes in the createrecipe.html template
	var ingredientidnumber = 5;
	var instructionidnumber = 3;
	
	// Adding a textbox for ingredient in the createrecipe.html template if the '+' button is pressed.
	$("#add-ingredient-button").on("click", function() {
	    $(".ingredient-textboxes").append('<input class="create-recipe-ingredient" id="ingredients-' + ingredientidnumber + '" type="text" name="ingredients-' + ingredientidnumber + '" placeholder="Ingredient" value/>');
	    ingredientidnumber++;
	});
	
	// Adding a textbox for instruction in the createrecipe.html template if the '+' button is pressed.
	$("#add-instruction-button").on("click", function() {
		$(".instruction-textboxes").append('<textarea class="create-recipe-instruction" id="instructions-' + instructionidnumber + '" placeholder="Instruction" name="instructions-' + instructionidnumber + '"></textarea>');
		instructionidnumber++;
	});
});