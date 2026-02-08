## 🚀 Backend Project 1 (Development)

*Innomatics Research Labs – Data Science Internship*

This repository contains a Flask-based web application developed to replicate the **core functionality of regex101.com**. The application allows users to input a test string and a regular expression, then displays all matching patterns found within the input text.

The objective of this task is to understand **Flask form handling, POST requests, template rendering, and regular expression processing** using Python, without focusing on advanced UI features or frontend styling.

---

## 📁 Project Structure

All assignment programs are organized as separate Python files:

```
📁 Sourav_419_Data-Science-with-Advanced-GENAI-Internship_Assignment_8
│
├── app.py
├── flask_task_2.png
└── templates
    └── index.html
```

Each file contributes directly to the functionality of the application.

---

## 🧩 Problem Statement

Visit and explore regex101.com and clone its **core functionality**. The application should ask the end user to enter a test string and a regular expression, and upon clicking the Submit button, display all the matched strings.

This task evaluates understanding of Flask routing, form submission, backend processing, and regex-based pattern matching.

---

## 🛠 Technologies Used

Python, Flask, HTML, and Python’s built-in `re` (regular expressions) module are used to build this application.

---

## ▶️ How the Application Works

The Flask application runs on a local development server and renders an HTML form to the user. The user provides a test string and a regular expression through the form. Upon submission, the data is sent to the backend using a POST request. The application processes the input using Python’s regular expression functions to extract all matches and returns the results to the browser dynamically. Invalid regular expressions are handled gracefully without breaking the application.

---

## ▶️ How to Run the Application

Ensure that Python is installed on your system. Install Flask by running the following command in the terminal or command prompt:  
pip install flask  

After installing Flask, navigate to the project directory and start the application using:  
python app.py  

Once the server starts, open a web browser and access the application at:  
http://127.0.0.1:5000/

---

## 📌 Example

Test String:  
Hello123 World456  

Regular Expression:  
\d+  

Output Displayed:  
123  
456  

The application displays all matched patterns as a list on the browser.

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Assignment** | Backend Project 1 (Development) |
| **Internship** | Data Science Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates the ability to build a Flask web application that handles user input through HTML forms, processes data using regular expressions, and dynamically renders results using templates. It reflects foundational backend development skills, proper request handling, and practical implementation of regex-based logic.


**This completes Internship Assignment => Backend Project 1 (Development) successfully.**

---

If you found this regex-based Flask project helpful, feel free to give it a ⭐
