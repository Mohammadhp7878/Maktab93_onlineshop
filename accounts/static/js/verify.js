document.getElementById("verify_form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    const userCode = document.getElementById("code").value;

    fetch("/verify_api/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": "{{ csrf_token }}" 
        },
        body: JSON.stringify({ code: userCode })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the API
        if (data.message === "Welcome") {
            window.location.href = "products/"; 
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error("Error verifying code:", error);
    });
});