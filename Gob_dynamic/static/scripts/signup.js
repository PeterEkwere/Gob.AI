$(document).ready(function () {
    //Function to show the loading spinner
    function showLoadingSpinner(){
        $("#loading-spinner").show();
    }

    // Function to hide the loading spinner
    function hideLoadingSpinner() {
        $("#loading-spinner").hide();
    }

    // Function to show a success message
    function showSuccessMessage() {
        $("#success-message").text("Account created successfully! Redirecting to login...");
    }

    // Event listener for the submit button
    $("#submitButton").on("click", function () {
        showLoadingSpinner()
        submitForm();
    })


    function submitForm() {
        var user_name = $("input[name='username']").val();
        var email = $("input[name='email']").val();
        var password = $("input[name='password']").val();
        var retypePassword = $("input[name='retypePassword']").val();

        // Validate the Form Fields
        var isValid = true;
    
        if (password !== retypePassword) {
            isValid = false;
            console.log("isValid is false")
            hideLoadingSpinner()
            $("#password, #retypePassword").addClass("invalid-input");
        } else {
            console.log("IsValid is true")
            $("#password, #retypePassword").removeClass("invalid-input");
        }
        
        // Make the Ajax Post Request
        if (isValid) {
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5001/api/v1/users",
                contentType: "application/json",
                data: JSON.stringify({
                    user_name: user_name,
                    email: email,
                    password: password
                }),
                success: function (data) {
                    // Handle success response
                    window.location.href = "/login";
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
        
    }
    
})

