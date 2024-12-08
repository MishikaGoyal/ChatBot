# Chatbot Project

## Overview
This is an AI-powered chatbot built using **Natural Language Processing (NLP)** techniques. It identifies user intents and responds accordingly.

## Features
- Supports multiple intents such as greetings, farewells, gratitude, and assistance.
- Predicts user intent using a neural network.
- Lightweight web-based frontend powered by Flask.

## Directory Structure
chatbot_project/ ├── app.py # Backend logic ├── intents.json # Dataset of intents ├── model/ │ ├── chatbot_model.h5 # Trained model │ ├── class_names.npy # Encoded class labels │ ├── training_labels.npy # Training labels ├── templates/ │ └── index.html # Web UI for chatbot ├── static/ │ └── style.css # Optional styling for the frontend ├── README.md # Project details ├── requirements.txt # Dependencies


## Setup Instructions
1. Clone the repository.
2. Install dependencies:
    pip install -r requirements.txt
3. Train the chatbot or use the pre-trained model (chatbot_model.h5).
4. Run the app:
    python app.py
5. Open your browser and visit http://127.0.0.1:5000/.
