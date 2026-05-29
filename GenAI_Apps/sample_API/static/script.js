// Function to handle pressing Enter key in input
function handleKeydown(event) {
    if (event.key === "Enter") {
        askQuestion();
    }
}

// Function to handle suggestion chip clicks
function useSuggestion(text) {
    document.getElementById("userInput").value = text;
    askQuestion();
}

// Core function to fetch and stream response
async function askQuestion() {
    const inputEl = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");
    const outputBox = document.getElementById("outputBox");
    const suggestions = document.getElementById("suggestions");
    
    const question = inputEl.value.trim();
    if (!question) return;

    // Reset input and disable UI
    inputEl.value = "";
    inputEl.disabled = true;
    sendBtn.disabled = true;
    suggestions.style.opacity = "0.5";
    suggestions.style.pointerEvents = "none";

    // Add User Message to output
    appendMessage(question, "user");

    // Add System (AI) Message skeleton for streaming
    const aiMessageEl = appendMessage("", "system");
    const aiContentEl = aiMessageEl.querySelector(".msg-content");
    aiContentEl.classList.add("streaming");

    try {
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "Failed to fetch response from server");
        }

        // Read stream chunks
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let done = false;
        let contentAccumulator = "";

        while (!done) {
            const { value, done: readerDone } = await reader.read();
            done = readerDone;
            
            if (value) {
                const chunkText = decoder.decode(value, { stream: !done });
                contentAccumulator += chunkText;
                aiContentEl.textContent = contentAccumulator;
                // Auto scroll
                outputBox.scrollTop = outputBox.scrollHeight;
            }
        }

    } catch (error) {
        console.error(error);
        aiContentEl.textContent = `Error: ${error.message}`;
        aiContentEl.style.color = "#ff5252";
    } finally {
        // Clean up and re-enable UI
        aiContentEl.classList.remove("streaming");
        inputEl.disabled = false;
        sendBtn.disabled = false;
        suggestions.style.opacity = "1";
        suggestions.style.pointerEvents = "auto";
        inputEl.focus();
        outputBox.scrollTop = outputBox.scrollHeight;
    }
}

// Helper function to append message bubble to UI
function appendMessage(text, sender) {
    const outputBox = document.getElementById("outputBox");
    
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}-msg animate-fade`;

    const avatarDiv = document.createElement("div");
    avatarDiv.className = "msg-avatar";
    avatarDiv.textContent = sender === "user" ? "U" : "✦";

    const contentDiv = document.createElement("div");
    contentDiv.className = "msg-content";
    contentDiv.textContent = text;

    msgDiv.appendChild(avatarDiv);
    msgDiv.appendChild(contentDiv);
    outputBox.appendChild(msgDiv);

    // Scroll to bottom
    outputBox.scrollTop = outputBox.scrollHeight;

    return msgDiv;
}
