const connectWebSocket = () => {
    const chatSocket = new WebSocket(
        (window.location.protocol === "https:" ? "wss://" : "ws://") + window.location.host + '/ws/chat/sala_de_guerra/'
    );

    chatSocket.onopen = function(e) {
        console.log('Conexão WebSocket aberta com sucesso!');
    };

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const chat = document.querySelector('#chat');
        const messageElement = document.createElement('p');
        messageElement.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
        chat.appendChild(messageElement);
    };

    chatSocket.onclose = function(e) {
        console.error('Conexão WebSocket fechada. Tentando reconectar em 5 segundos...');
        setTimeout(connectWebSocket, 2000);  // Tenta reconectar após 2 segundos
    };

    chatSocket.onerror = function(e) {
        console.error('Erro na conexão WebSocket:', e);
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        const messageInput = document.querySelector('#chat-message-input');
        const message = messageInput.value;
        const username = document.querySelector('#username').value;

        if (chatSocket.readyState === WebSocket.OPEN) {
            console.log('Enviando mensagem:', { message, username });
            chatSocket.send(JSON.stringify({
                'message': message,
                'username': username,
            }));
            messageInput.value = '';
        } else {
            console.error('WebSocket não está conectado.');
        }
    };
};

// Inicia a conexão WebSocket
connectWebSocket();