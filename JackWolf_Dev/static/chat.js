var ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function(event) {
    var messageData = JSON.parse(event.data);
    var messages = document.getElementById('chat');
    var message = document.createElement('div');
    message.classList.add('message');
    message.classList.add(messageData.sender === 'user' ? 'user' : 'bot');
    message.textContent = messageData.message;
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight; // Scroll to the latest message
};

document.getElementById('messageForm').addEventListener("submit", function() {
    document.getElementById("messageInput").value = ''; // Clear the input after sending
    document.getElementById("fileInput").value = '';   // Clear the file input
});
