 
    <script>
$(document).ready(function () {
            // catch the form's submit event
            $('#id_username').keyup(function(e) {
                // create an AJAX call
                $.ajax({
                    data: $(this).serialize(), // get the form data
                    url: "{% url 'checkuser' %}",
                    // on success
                    success: function (response) {
                        if (response.is_taken == true) {
                           
                            $('#error').html("Username is already taken!")
                        }
                        else{
                            $('#error').html("")
                        }

                    },
                    // on error
                    error: function (response) {
                        // alert the error if any error occured
                        console.log(response.responseJSON.errors)
                    }
                });

                return false;
            });
              $('#id_email').keyup(function(e) {
                // create an AJAX call
                var email = $(this).val().trim();
                if(email != ''){
                $.ajax({
                    data: $(this).serialize(), // get the form data
                    url: "{% url 'checkuser' %}",
                    // on success
                    success: function (response) {
                        if (response.email_taken == true) {
                            
                            $('#emailerror').html("Email is already in use!")
                        }
                        else{
                            $('#emailerror').html("")
                        }

                    },
                    // on error
                    error: function (response) {
                        // alert the error if any error occured
                        console.log(response.responseJSON.errors)
                    }
                });
              }

                return false;
            });
        })
    </script>
