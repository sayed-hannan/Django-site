$(document).ready(function () {
    // Get the URL from a data attribute
    var createCourseURL = $("#create-course-form").data('create-course-url');

    $("#create-course-button").click(function () {
        // Serialize the form data to send via AJAX
        var formData = $("#create-course-form").serialize();

        // Send an AJAX POST request to your view
        $.ajax({
            type: "POST",
            url: createCourseURL,
            data: formData,
            beforeSend: function (xhr) {
                // Include the CSRF token in the headers
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function (response) {
                if (response.success) {
                    // Display a success message or perform any other action
                    alert("Course created successfully!");
                } else {
                    // Display form validation errors or handle the error case
                    alert("Course creation failed. Please check the form.");
                }
            },
            error: function () {
                // Handle AJAX error
                alert("An error occurred while creating the course.");
            }
        });
    });

    // Function to get the CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});







// module_script.js
$(document).ready(function () {
    // Get the URL from a data attribute
    var createModuleURL = $("#create-module-form").data('create-module-url');

    $("#create-module-button").click(function () {
        // Serialize the form data to send via AJAX
        var formData = $("#create-module-form").serialize();

        // Send an AJAX POST request to your view
        $.ajax({
            type: "POST",
            url: createModuleURL,
            data: formData,
            beforeSend: function (xhr) {
                // Include the CSRF token in the headers
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function (response) {
                if (response.success) {
                    // Display a success message or perform any other action
                    alert("Module created successfully!");
                } else {
                    // Display form validation errors or handle the error case
                    alert("Module creation failed. Please check the form.");
                }
            },
            error: function () {
                // Handle AJAX error
                alert("An error occurred while creating the module.");
            }
        });
    });

    // Function to get the CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});




