// chat/static/chat/chat.js
document.addEventListener("DOMContentLoaded", () => {
    const chatLog = document.getElementById('chat-log');
    const chatMessageInput = document.getElementById('chat-message-input');
    const chatMessageSubmit = document.getElementById('chat-message-submit');
    const usersList = document.getElementById('users-list');
    const profileForm = document.getElementById('profile-form');
    
    const roomName = "general";  // This could be dynamic
    const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        chatLog.value += `${data.message}\n`;
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    chatMessageSubmit.onclick = function() {
        const message = chatMessageInput.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        chatMessageInput.value = '';
    };

    // Fetch users and populate the users list
    fetch('/chat/users/list/')
        .then(response => response.json())
        .then(data => {
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = user.username;
                usersList.appendChild(li);
            });
        });

    // Handle profile form submission
    profileForm.onsubmit = function(event) {
        event.preventDefault();
        const formData = new FormData(profileForm);
        
        fetch('/chat/profile/update/', {
            method: 'PUT',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            alert('Profile updated successfully');
        })
        .catch(error => {
            console.error('Error updating profile:', error);
        });
    };

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
