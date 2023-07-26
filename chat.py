import numpy as np
import json
from nltk_methods import *
import tensorflow as tf
from student import Student
import sqlite3


# Connect to the database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
# c.execute('''DROP TABLE users''')
c.execute('''CREATE TABLE IF NOT EXISTS users
             ("CIN" TEXT PRIMARY KEY,
             "Nom" TEXT,
             "Prénom" TEXT,
             "Date de naissance" TEXT,
             "Système d'études" TEXT,
             "Série" TEXT,
             "Option" TEXT)''')

# Function to load intents and preprocess data
with open('D:\Downloads\Chatbot Project\pytorch chatbot\intents.json', 'r') as f:
    intents = json.load(f)

def load_intents(intents):
    
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

    return all_words, tags, xy

# Load intents and preprocess data
# file_path = 'D:\Downloads\Chatbot Project\pytorch chatbot\intents.json'
all_words, tags, xy = load_intents(intents)


# Function to get responses for non-"answer" intents
def get_random_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            responses = intent["responses"]
            break
    return np.random.choice(responses)


# Function to get predictions from the model
def get_response(model, user_input):
    # Tokenize and preprocess the user's input
    user_input = tokenize(user_input)
    user_input = bag_of_words(user_input, all_words)
    user_input = np.array([user_input])
    print("User input: ", user_input)
    print("xy : ", xy)

    # Get prediction probabilities from the model
    predictions = model.predict(user_input)
    print("predictions :", predictions)
    
    # Get the index of the highest probability prediction
    predicted_index = np.argmax(predictions)
    print("predicted index : ", predicted_index)
    
    # Get the corresponding tag for the highest probability prediction
    predicted_tag = tags[predicted_index]
    print("predicted tag : ", predicted_tag)

    
    if predicted_tag == "inscription":
       
        s = Student()
        c.execute("INSERT INTO users (CIN, Nom, Prénom, 'Date de naissance', \"Système d'études\", Série, Option) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (s.cin, s.nom.upper(), s.prenom.capitalize(), s.birthdate, s.sys_etudes.capitalize(), s.serie, s.option.upper()))
        conn.commit()
        print("Merci.")
    else: 
        return get_random_response(predicted_tag)



# Load the trained model
model = tf.keras.models.load_model("chatbot_model")

# Example usage
print("\nBot: Bonjour ! Je suis le chatbot de notre université, et je suis à votre service, vous pouvez appuyez sur 'Q' à tout instant pour arrêter la discussion, maintenant discutons !")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "q":
        break
    response = get_response(model, user_input)
    print("Bot: ", response, "\n")

conn.close()