document.getElementById("login_form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    const phoneNumber = document.getElementById("phone_number").value;

    // Send the data to the API using Fetch or Axios
    fetch("/login_api/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": "{{ csrf_token }}" 
        },
        body: JSON.stringify({ phone_number: phoneNumber })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the API
        if (data.message === "OTP sent successfully") {
            // Optionally, you can redirect the user to the verify page or show a success message
            window.location.href = "/verify/"; 
        } else {
            // Handle error response
            console.error("Error sending OTP:", data);
        }
    })
    .catch(error => {
        console.error("Error sending request:", error);
    });
});