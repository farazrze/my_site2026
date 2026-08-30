const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const message = document.getElementById("loginMessage");

        if (username === "admin" && password === "1234") {

            message.textContent = "Login successful!";

            setTimeout(function() {
                window.location.href = "app.html";
            }, 500);

        } else {

            message.textContent = "Invalid username or password.";

        }

    });

}


/* LOGOUT */

const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {

    logoutBtn.addEventListener("click", function() {
        window.location.href = "login.html";
    });

}