from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatterbot = ChatBot("chatterbot")

chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("bot/chatterbot.json")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatterbot.get_response(userText))


if __name__ == "__main__":
    app.run()
