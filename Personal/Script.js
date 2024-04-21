document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contact-form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get form values
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        // Here you can add code to send the form data to your backend or display it in some way
        console.log("Name:", name);
        console.log("Email:", email);
        console.log("Message:", message);

        // Optionally, you can clear the form fields after submission
        form.reset();
    });
});
