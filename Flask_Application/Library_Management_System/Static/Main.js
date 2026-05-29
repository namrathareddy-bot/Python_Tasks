// LOGIN
function login() {
    fetch("http://127.0.0.1:5001/api/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.message) window.location.href = "/home";
        else alert("Invalid login");
    });
}

// ISSUE BOOK
function issueBook() {
    fetch("http://127.0.0.1:5001/api/issue", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            book_id: document.getElementById("book_id").value,
            user: document.getElementById("user").value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message || data.error));
}

// RETURN BOOK
function returnBook() {
    fetch("http://127.0.0.1:5001/api/return", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            book_id: document.getElementById("book_id").value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}