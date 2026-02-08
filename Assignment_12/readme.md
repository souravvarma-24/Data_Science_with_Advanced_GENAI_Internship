## 🚀 Sentiment Analysis of Real-time Flipkart Product Reviews

---

**Innomatics Research Labs – Data Science Internship**

This repository contains an end-to-end **Sentiment Analysis project** built on real-time Flipkart product reviews. The project focuses on classifying customer reviews as **Positive or Negative** and understanding customer pain points through sentiment-based analysis.

A trained machine learning model is integrated into a **Streamlit web application** that performs real-time sentiment prediction based on user-provided review text.

---

## 🧩 Problem Statement

The objective of this project is to analyze customer reviews from Flipkart and classify them into positive or negative sentiment. By performing sentiment analysis, the project aims to identify product strengths and customer dissatisfaction patterns.

The solution includes data preprocessing, feature extraction, model training, evaluation, and deployment of the trained model through a Streamlit web application.

---

## 📁 Project Structure

All project files are organized as shown below:

```
📁 Sourav_419_Data-Science-with-Advanced-GENAI-Internship_Assignment_12
│
├── app.py
├── flipkart_sentiment.ipynb
├── requirements.txt
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── review_good.png
└── review_bad.png
```

Each file contributes directly to the sentiment analysis and application workflow.

---

## 🛠 Technologies Used

- Python  
- Pandas & NumPy  
- Natural Language Processing (NLP)  
- Scikit-learn  
- TF-IDF Vectorization  
- Streamlit  
- Pickle  

---

## ▶️ Project Workflow

1. Load and explore the Flipkart reviews dataset.
2. Clean and preprocess review text by removing noise and normalizing text.
3. Convert textual data into numerical features using TF-IDF.
4. Train a sentiment classification model on the processed data.
5. Evaluate the model performance using appropriate metrics.
6. Save the trained model and vectorizer.
7. Integrate the model into a Streamlit web application.
8. Perform real-time sentiment prediction on user input.

---

## ▶️ How the Application Works

The Streamlit application loads the trained sentiment classification model and TF-IDF vectorizer. When a user enters a review, the text is preprocessed and transformed into numerical features. The model then predicts the sentiment of the review and displays whether it is **Positive** or **Negative**.

This allows real-time sentiment inference without retraining the model.

---

## ▶️ How to Run the Application

Ensure Python is installed on your system. Install the required dependencies using:

pip install -r requirements.txt

Run the Streamlit application using:

streamlit run app.py

The application will open in your browser for real-time sentiment analysis.

---

## 📌 Features Implemented

- Text preprocessing and normalization  
- TF-IDF based feature extraction  
- Machine learning model for sentiment classification  
- Real-time sentiment prediction using Streamlit  
- User-friendly web interface  

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Project** | Sentiment Analysis of Real-time Flipkart Product Reviews |
| **Internship** | Data Science Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates a complete sentiment analysis pipeline, from data preprocessing and model training to real-time deployment using Streamlit. It highlights practical skills in NLP, machine learning, and application integration, aligned with real-world data science workflows.

---

**This completes Internship Assignment => Sentiment Analysis of Real-time Flipkart Product Reviews successfully.**

---

## Your support matters! If this repository helped you, please leave a ⭐.
