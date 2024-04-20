document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // You can use the FormData API to gather form data
        const formData = new FormData(form);

        // Send an AJAX request to the server
        $.ajax({
            url: '/submit-contact/', // Use the correct URL for your contact_view
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                if (data.success) {
                    form.style.display = 'none'; // Hide the form
                    successMessage.style.display = 'block'; // Display the success message
                    errorMessage.style.display = 'none'; // Hide the error message
                } else {
                    errorMessage.style.display = 'block'; // Display the error message
                }
            },
            error: function () {
                console.error('Error: An error occurred');
                errorMessage.style.display = 'block'; // Display the error message
            }
        });
    });
});

