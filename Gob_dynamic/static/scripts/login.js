$(document).ready(function () {
    //Function to show the loading spinner
    function showLoadingSpinner(){
        $("#loading-spinner").show();
    }

    // Function to hide the loading spinner
    function hideLoadingSpinner() {
        $("#loading-spinner").hide();
    }

    // Event listener for the submit button
    $("#submitButton").on("click", function () {
        showLoadingSpinner()
        submitForm();
    })


    function submitForm() {
        var email = $("input[name='email']").val();
        var password = $("input[name='password']").val();
        
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5001/api/v1/login",
            contentType: "application/json",
            data: JSON.stringify({
                email: email,
                password: password
            }),
            success: function (data) {
                // Handle success response
                window.location.href = "/dashboard";
                console.log("Success:", data)
            },
            error: function (error) {
                // Handle error response
                console.log("Error:", error);
            },
            complete: function () {
                // Hide the loading spinner after 7 seconds
                setTimeout(function () {
                    hideLoadingSpinner();
                }, 7000);
            },
        });
        
    }
    
})

