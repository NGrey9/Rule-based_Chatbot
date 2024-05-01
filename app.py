import json
from flask import Flask, render_template, request, jsonify
from RuleBasedChatbot import getAnswer

with open("./personal.json", 'r') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    userText = request.form["msg"]
    userText = userText.lower()
    intents = data['intents']
    answer = getAnswer(userText, intents)
    return answer


if __name__ == '__main__':
    app.run(debug=True)