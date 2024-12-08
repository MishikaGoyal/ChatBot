document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    // Function to add a message to the chatbox
    function addMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.innerHTML = `<p>${text}</p>`;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
    }

    // Handle send button click
    sendBtn.addEventListener("click", async () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            addMessage("user", userMessage); // Add user message
            userInput.value = ""; // Clear input

            // Fetch response from chatbot backend
            try {
                const response = await fetch("/get-response", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: userMessage }),
                });
                const data = await response.json();
                addMessage("bot", data.response); // Add bot response
            } catch (error) {
                addMessage("bot", "Error connecting to the server. Please try again.");
            }
        }
    });

    // Handle Enter key press
    userInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            sendBtn.click();
        }
    });
});
