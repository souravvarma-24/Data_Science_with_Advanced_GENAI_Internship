## 🚀 Final Project (For Advance Participants) - URL Shortner Application

**Innomatics Research Labs – Data Science Internship**

This repository contains an **Advanced URL Shortener Web Application** developed using Flask.  
The application implements **user authentication, session management, protected routes, and user-specific URL history**, making it comparable to real-world backend systems.

Registered users can sign up, log in, shorten URLs, view only their own shortened URLs, and securely log out of the application.

---

## 🧩 Problem Statement

Develop an **Advanced URL Shortener Web Application** that:
- Allows users to register and log in
- Restricts URL shortening to authenticated users
- Stores original and shortened URLs per user
- Displays user-specific URL history
- Redirects shortened URLs to their original destinations

The application must be implemented using Flask with proper database integration and authentication mechanisms.

---

## 📁 Project Structure

All submission files are organized as shown below:

```
📁 Sourav_419_Data-Science-with-Advanced-GENAI-Internship_Assignment_11
│
├── app.py
├── app.db
├── URL Shortener Web Application (Advanced Version).pdf.pdf
├── flask_task5a.png
├── flask_task5b.png
├── flask_task5c.png
└── templates
    ├── login.html
    ├── signup.html
    ├── index.html
    └── history.html
```

Each file contributes directly to fulfilling the advanced project requirements.

---

## 🛠 Technologies Used

- Python  
- Flask  
- Flask-Login  
- Flask-SQLAlchemy  
- HTML  
- SQLite  
- Werkzeug (for password hashing)

---

## ▶️ Application Workflow

1. A new user signs up using a username and password.
2. The password is securely hashed and stored in the database.
3. The user logs in using valid credentials.
4. After login, the user can enter a long URL and generate a shortened URL.
5. The shortened URL is stored along with the logged-in user’s identity.
6. The user can view only **their own URL history**.
7. Clicking a shortened URL redirects to the original URL.
8. The user can log out, ending the session.

All sensitive routes are protected and accessible only after authentication.

---

## ▶️ How the Application Works

The application uses **Flask-Login** to manage authentication and protect routes.  
User credentials and URL mappings are stored in an SQLite database. Each shortened URL is linked to the user who created it, ensuring user-specific access control.

When a shortened URL is accessed, Flask retrieves the original URL from the database and redirects the user safely.

---

## ▶️ How to Run the Application

Ensure Python is installed on your system. Install the required dependencies:

pip install flask flask_sqlalchemy flask_login

Run the application using:

python app.py

Open a browser and access the application at:

http://127.0.0.1:5000/login

---

## 📌 Features Implemented

- User signup and login system  
- Secure password hashing  
- Session management  
- Protected routes using Flask-Login  
- URL shortening and redirection  
- User-specific URL history  
- SQLite database integration  

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Assignment** | Final Project (For Advance Participants) - URL Shortner Application |
| **Internship** | Data Science Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates the implementation of a **secure and user-specific URL Shortener web application** using Flask. It covers authentication, session handling, protected routes, database relationships, and backend logic aligned with real-world application requirements.

---

**This completes Internship Assignment => Final Project (For Advance Participants) - URL Shortner Application successfully.**

---

## Your support matters! If this repository helped you, please leave a ⭐.
