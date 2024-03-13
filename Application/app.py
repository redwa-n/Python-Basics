from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")


app = Flask(__name__)

# Create a chatbot instance
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(english_bot)

# Train the chatbot on the english corpus
trainer.train("chatterbot.corpus.english")

# Define a route for the chatbot endpoint
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(english_bot.get_response(user_text))

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
