from flask import Flask, render_template, request, jsonify
import spacy
import tensorflow as tf
import numpy as np
import pickle
import json

# Initialize Flask app
app = Flask(__name__)

# Load necessary resources
# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Load the trained chatbot model
model = tf.keras.models.load_model("model/chatbot_model.h5")

# Load tokenizer and class names
with open("model/tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)
class_names = np.load("model/class_names.npy", allow_pickle=True)

# Load intents data
with open("intents.json") as file:
    intents_data = json.load(file)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot responses
@app.route("/get-response", methods=["POST"])
def get_response():
    try:
        # Extract user message from request
        user_message = request.json.get("message", "")
        
        # Tokenize and pad the user message
        sequence = tokenizer.texts_to_sequences([user_message])
        padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(sequence, padding="post", maxlen=20)
        
        # Get prediction from the model
        prediction = model.predict(padded_sequence)
        predicted_class = class_names[np.argmax(prediction)]
        
        # Retrieve response based on the predicted intent
        bot_response = "I'm sorry, I don't understand. Can you rephrase?"  # Default response
        for intent in intents_data["intents"]:
            if intent["tag"] == predicted_class:
                bot_response = np.random.choice(intent["responses"])
                break
        
        # Return the response as JSON
        return jsonify({"response": bot_response})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"response": "Oops! Something went wrong. Please try again."})

# Main block to run the app
if __name__ == "__main__":
    app.run(debug=True)
