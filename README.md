# University Chatbot Project

![Chatbot Demo](chatbot_demo.gif)

## Overview

Welcome to the University Chatbot project! This repository contains the code for developing a state-of-the-art Chatbot designed to enhance the engagement and communication experience for prospective students at [University Name]. The Chatbot is implemented in Python and utilizes natural language processing (NLP) techniques along with machine learning models to deliver accurate and contextually relevant responses.

## Project Overview

The goal of this project is to create an intelligent Chatbot that can efficiently handle inquiries from potential students, providing them with personalized information about the university's programs, admission process, contact details, and more. The Chatbot has been trained on a diverse dataset of user intents and responses, allowing it to understand various patterns and engage in meaningful conversations with users.

## Technologies Used

- **Python:** The project is entirely built on Python, which serves as the foundation for data processing, machine learning, and integration with other libraries.
- **Natural Language Processing (NLP):** We employ the Natural Language Toolkit (NLTK) library to preprocess and analyze text inputs, making it easier for the Chatbot to understand variations in word forms and improve user interactions.
- **TensorFlow/Keras:** To build and train the machine learning model, we utilize TensorFlow with the Keras API. This enables us to create a Sequential model that can classify user intents and generate responses accordingly.
- **SQLite Database:** We use an SQLite database to store user information and facilitate personalized interactions.
- **Flask:** Flask is a lightweight web application framework in Python that we used to integrate the Chatbot into a website. It allows us to create a web server and handle user interactions through HTTP requests.

## How the Chatbot Works

1. **User Input:** Users can interact with the Chatbot through text input.
2. **Preprocessing:** The user input is tokenized and preprocessed using NLTK. Stemming and lemmatization are applied to handle different word forms.
3. **Intent Classification:** The preprocessed input is then fed into the trained TensorFlow/Keras model, which classifies the user's intent (e.g., greetings, inquiries about programs, admission process, etc.).
4. **Response Generation:** Based on the predicted intent, the Chatbot generates an appropriate response using predefined responses or specific functions for certain intents (e.g., providing contact information, guiding through the admission process).
5. **Personalized Interaction:** The Chatbot can provide personalized responses, tailored to the user's interests or selected program of study.

## How to Use the Chatbot

1. Install the required libraries: `numpy`, `nltk`, `tensorflow`, `keras`, `sqlite3`, and `flask`.
2. Train the Chatbot by running the `train.py` script. This will preprocess the data, build the model, and save it as `chatbot_model`.
3. To interact with the Chatbot on a website, run the `app.py` script, which contains the Flask application. The Chatbot will be accessible through the website.
4. Alternatively, you can still use the command-line version of the Chatbot by running the `chat.py` script.

## Integrating the Chatbot into a Website with Flask

1. Install Flask using `pip install flask`.
2. Create an HTML form on your website that allows users to input their questions and submit them to the Chatbot.
3. Use Flask to handle user inputs from the form and pass them to the Chatbot for processing.
4. Display the Chatbot's responses back to the user on the website.
5. You can use AJAX to enable real-time interactions with the Chatbot without the need to refresh the entire page.

## Future Enhancements

This Chatbot project has the potential for further enhancements and customization. Some future ideas include:

- Implementing more advanced NLP techniques to improve the Chatbot's understanding of complex queries.
- Incorporating a sentiment analysis component to gauge user satisfaction and improve responses.
- Integration with external APIs to provide real-time data, such as event schedules or admission deadlines.

