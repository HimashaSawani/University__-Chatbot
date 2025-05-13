// static/js/script.js

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    const chatHistory = document.getElementById('chat-history');
    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message');
    userMessage.innerText = "You: " + userInput;
    chatHistory.appendChild(userMessage);

    // Clear the input field
    document.getElementById('user-input').value = "";

    // Send user input to Flask backend (via POST request)
    fetch('/chatbot', {
        method: 'POST',
        body: new URLSearchParams({
            'user_input': userInput
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = document.createElement('div');
        botResponse.classList.add('bot-message');
        botResponse.innerText = "Bot: " + data.response;
        chatHistory.appendChild(botResponse);

        // Scroll to the bottom of chat history
        chatHistory.scrollTop = chatHistory.scrollHeight;
    });
}

// A simple function that mimics chatbot response (for testing only)
// This will be replaced by Flask backend logic
function getBotResponse(userInput) {
    if (userInput.toLowerCase().includes("hello")) {
        return "Hello! How can I assist you today?";
    } else {
        return "I'm sorry, I don't understand your question.";
    }
}
