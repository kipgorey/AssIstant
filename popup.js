window.addEventListener("load", function() {
    document.getElementById("user-input-form").addEventListener("submit", function(event) {
        // Prevent the form from submitting normally
        event.preventDefault();

        // Get the user's input
        var userInput = document.querySelector(".input-field").value;

        // Log the user's input
        console.log(userInput);

        // Send the user's input to your Python backend
        fetch('http://localhost:5000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({input: userInput})
        }).then(response => response.json())
        .then(data => {
            // Handle the response from the server
            console.log('Response:', data);
            let url = data.url;

            chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
                // Update the URL of the active tab
                chrome.tabs.update(tabs[0].id, { url: url });
            });

        }).catch(error => {
            console.error('Error:', error);
        });
    });
});
