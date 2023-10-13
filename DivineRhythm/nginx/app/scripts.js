document.getElementById('sendButton').addEventListener('click', function() {
    const userMessage = document.getElementById('userInput').value;
    if(userMessage) {
        addMessageToChatbox('User: ' + userMessage, 'user');
        fetch('http://localhost:8088/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: userMessage,
                sender: 'user',
            }),
        })
        .then(response => response.json())
        .then(data => {
            data.forEach((message) => {
                addMessageToChatbox('Bot: ' + message.text, 'bot');
            });
        })
        .catch((error) => {
            console.error('Error:', error);
            addMessageToChatbox('Bot: Sorry, I am facing some issues right now.', 'bot');
        });
    }
    document.getElementById('userInput').value = '';
});

function addMessageToChatbox(message, sender) {
    const chatbox = document.getElementById('chatbox');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ' + (sender === 'user' ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}
