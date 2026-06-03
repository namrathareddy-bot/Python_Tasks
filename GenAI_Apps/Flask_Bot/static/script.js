function handleKeydown(event) {
    if (event.key === "Enter") {
        askQuestion();
    }
}

function useSuggestion(text) {
    document.getElementById("userInput").value = text;
    askQuestion();
}

function toggleAccordion(element) {
    const parent = element.parentElement;
    parent.classList.toggle("open");
    const icon = element.querySelector(".toggle-icon");
    if (parent.classList.contains("open")) {
        icon.textContent = "▼";
    } else {
        icon.textContent = "▶";
    }
}

async function askQuestion() {
    const inputEl = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");
    const outputBox = document.getElementById("outputBox");
    const suggestions = document.getElementById("suggestions");
    
    const question = inputEl.value.trim();
    if (!question) return;

    inputEl.value = "";
    inputEl.disabled = true;
    sendBtn.disabled = true;
    suggestions.style.opacity = "0.5";
    suggestions.style.pointerEvents = "none";

    appendMessage(question, "user");

    const loaderEl = appendLoader();

    try {
        const response = await fetch("/api/chat-db", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        loaderEl.remove();

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "Server error occurred while querying database.");
        }

        const data = await response.json();
        appendResponse(data);

    } catch (error) {
        console.error(error);
        if (loaderEl) loaderEl.remove();
        appendMessage(`Error: ${error.message}`, "system", true);
    } finally {
        inputEl.disabled = false;
        sendBtn.disabled = false;
        suggestions.style.opacity = "1";
        suggestions.style.pointerEvents = "auto";
        inputEl.focus();
        outputBox.scrollTop = outputBox.scrollHeight;
    }
}

function appendMessage(text, sender, isError = false) {
    const outputBox = document.getElementById("outputBox");
    
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}-msg animate-fade`;

    const avatarDiv = document.createElement("div");
    avatarDiv.className = "msg-avatar";
    avatarDiv.textContent = sender === "user" ? "U" : "✦";

    const contentDiv = document.createElement("div");
    contentDiv.className = "msg-content";
    contentDiv.textContent = text;
    if (isError) {
        contentDiv.style.color = "#ff4d4d";
        contentDiv.style.border = "1px solid rgba(255, 77, 77, 0.2)";
        contentDiv.style.background = "rgba(255, 77, 77, 0.05)";
    }

    msgDiv.appendChild(avatarDiv);
    msgDiv.appendChild(contentDiv);
    outputBox.appendChild(msgDiv);

    outputBox.scrollTop = outputBox.scrollHeight;
    return msgDiv;
}

function appendLoader() {
    const outputBox = document.getElementById("outputBox");
    
    const msgDiv = document.createElement("div");
    msgDiv.className = "message system-msg loader-msg animate-fade";

    const avatarDiv = document.createElement("div");
    avatarDiv.className = "msg-avatar";
    avatarDiv.textContent = "✦";

    const contentDiv = document.createElement("div");
    contentDiv.className = "msg-content";
    
    const spinner = document.createElement("div");
    spinner.className = "spinner";
    
    const textNode = document.createTextNode(" Analyzing schema and querying MySQL...");

    contentDiv.appendChild(spinner);
    contentDiv.appendChild(textNode);
    msgDiv.appendChild(avatarDiv);
    msgDiv.appendChild(contentDiv);
    outputBox.appendChild(msgDiv);

    outputBox.scrollTop = outputBox.scrollHeight;
    return msgDiv;
}

function appendResponse(data) {
    const outputBox = document.getElementById("outputBox");
    
    const msgDiv = document.createElement("div");
    msgDiv.className = "message system-msg animate-fade";

    const avatarDiv = document.createElement("div");
    avatarDiv.className = "msg-avatar";
    avatarDiv.textContent = "✦";

    const contentDiv = document.createElement("div");
    contentDiv.className = "msg-content";

    const textEl = document.createElement("div");
    textEl.className = "response-text";
    textEl.textContent = data.response;
    contentDiv.appendChild(textEl);

    const sqlDetails = document.createElement("div");
    sqlDetails.className = "sql-details";

    const header = document.createElement("div");
    header.className = "details-header";
    header.setAttribute("onclick", "toggleAccordion(this)");
    header.innerHTML = `<span>⚙️ View SQL Execution details</span><span class="toggle-icon">▶</span>`;
    sqlDetails.appendChild(header);

    const body = document.createElement("div");
    body.className = "details-body";

    const sqlTitle = document.createElement("div");
    sqlTitle.className = "code-title";
    sqlTitle.textContent = "Generated SQL Query";
    body.appendChild(sqlTitle);

    const sqlPre = document.createElement("pre");
    sqlPre.className = "code-block";
    sqlPre.textContent = data.sql;
    body.appendChild(sqlPre);

    const resTitle = document.createElement("div");
    resTitle.className = "code-title";
    resTitle.textContent = data.error ? "Execution Error" : "Fetched Database Rows";
    body.appendChild(resTitle);

    const resPre = document.createElement("pre");
    if (data.error) {
        resPre.className = "code-block";
        resPre.style.color = "#ff4d4d";
        resPre.textContent = data.error;
    } else {
        resPre.className = "data-block";
        resPre.textContent = JSON.stringify(data.results, null, 2);
    }
    body.appendChild(resPre);

    sqlDetails.appendChild(body);
    contentDiv.appendChild(sqlDetails);
    
    msgDiv.appendChild(avatarDiv);
    msgDiv.appendChild(contentDiv);
    outputBox.appendChild(msgDiv);

    outputBox.scrollTop = outputBox.scrollHeight;
}
