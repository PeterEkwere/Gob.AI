$(document).ready(function () {
    function showLoadingSpinner(){
        $("#loading-spinner").show();
    }

    // Function to hide the loading spinner
    function hideLoadingSpinner() {
        $("#loading-spinner").hide();
    }

    // Function to show the recipe result
    function showRecipeResult() {
        $("#result-recipe").show();
    }
    // Funtion to hide recipe result
    function hideRecipeResult() {
        $("#result-recipe").hide()
    }
    // Event listener for the submit button
    $("#Generatebtn").on("click", function () {
        showLoadingSpinner();
        hideRecipeResult();
        submitForm();
    })



    function submitForm() {
        var ingredients = $("input[name='enter']").val();
        
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5001/api/v1/recipe",
            contentType: "application/json",
            data: JSON.stringify({
                ingredients: ingredients
            }),
            success: function (data) {
                
                // Handle success response
                console.log('Success');
                //populateRecipeResult(data)
                
            },
            error: function (error) {
                // Handle error response
                console.log("Error:", error);
            },
            complete: function () {
                //Hide the loading spinner after 7 seconds
                setTimeout(function () {
                    hideLoadingSpinner();
                    showRecipeResult();
                }, 5000);
            },
        });

    }

    function populateRecipeResult(responseData) {

        // Parse the JSON string to an array of objects
        const recipes = JSON.parse(JSON.parse(responseData));

        // Get a random index
        const randomIndex = Math.floor(Math.random() * recipes.length);

        // Access the first recipe
        const firstRecipe = recipes[randomIndex];
       
        // Extract relevant information
        const recipeName = firstRecipe.title;
        const ingredients = firstRecipe.ingredients;
        const instructions = firstRecipe.instructions;
        console.log("ingredients are" + ingredients)
        console.log("instructions are" + instructions)
        console.log("REcipe name is" + recipeName)
        // Get the recipe result div
        const recipeResultDiv = document.querySelector('.recipe-result');
        // Split instructions
        pattern = new RegExp('/\.\s+/')
        const stepsArray = instructions.split('.');
        // Remove empty strings and trim each step
        const filteredStepsArray = stepsArray.filter(step => step.trim() !== '');
        // Split Ingredients
        const ingredientsArray = ingredients.split('|');

        console.log("steps array is ", filteredStepsArray)

        // Generate Ingredients HTML
        const ingredientsHTML = ingredientsArray.map(ingredient => `<li>${ingredient.trim()}</li>`).join('');


        // Generate Steps HTML using a for loop
        let stepsHTML = '';
        for (let i = 0; i < filteredStepsArray.length; i++) {
            stepsHTML += `<li>${filteredStepsArray[i]}</li>`;
        }

        
        // Create and append HTML Content
        recipeResultDiv.innerHTML = `
        <h2 class="result-h2">${recipeName}</h2>
        
        <div class="ingredients-steps">
            <div class="ingredients">
                <h3 class="ingredients-h3">Ingredients</h3>
                <ul class="ingredients-ul">
                    ${ingredientsHTML}
                </ul>
            </div>
        
            <div class="steps">
                <h3 class="steps-h3">Steps</h3>
                <ol class="steps-ol">
                    ${stepsHTML}
                </ol>
            </div>     
        </div>`;
    }

})