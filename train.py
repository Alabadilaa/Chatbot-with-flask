import numpy as np
import json
from nltk_methods import *
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models, losses


# Load intents and preprocess data
with open('D:\Downloads\Chatbot Project\pytorch chatbot\intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ["?", "-", ";", ",", ".", "/", "!", "_"]
all_words = [stem(w) for w in all_words if w not in ignore_words]

all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

# Create the input (X) and output (y) data
X_train = []
y_train = []
responses = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)
    responses.append(intent["responses"])

X_train = np.array(X_train)
y_train = np.array(y_train)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val, responses_train, responses_val = train_test_split(X_train, y_train, responses, test_size=0.2, random_state=42)


num_epochs = 500
batch_size = 16
learning_rate = 0.0001
input_size = len(X_train[0])
hidden_size = 4
output_size = len(tags)

# Build the model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(input_size,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(output_size, activation='softmax')
])

# Compile the model
model.compile(loss=losses.SparseCategoricalCrossentropy(from_logits=True), optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=num_epochs, batch_size=batch_size)

# Save the model
model.save("chatbot_model")

print("Training complete. Model saved.")