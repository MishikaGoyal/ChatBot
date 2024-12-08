import json
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load intents data
with open("intents.json") as file:
    data = json.load(file)

# Extract training data
training_sentences = []
training_labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        training_sentences.append(pattern)
        training_labels.append(intent["tag"])

# Encode labels
label_encoder = LabelEncoder()
training_labels = label_encoder.fit_transform(training_labels)

# Save class names
np.save("model/class_names.npy", label_encoder.classes_)

# Tokenize and pad sequences
vocab_size = 1000
max_length = 20
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding="post")

# Save tokenizer
with open("model/tokenizer.pkl", "wb") as file:
    pickle.dump(tokenizer, file)

# Build the model
model = Sequential([
    Dense(128, input_shape=(max_length,), activation="relu"),
    Dropout(0.5),
    Dense(64, activation="relu"),
    Dropout(0.5),
    Dense(len(label_encoder.classes_), activation="softmax")
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(padded_sequences, np.array(training_labels), epochs=200, verbose=1)

# Save the trained model
model.save("model/chatbot_model.h5")
