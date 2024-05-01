import re
from nltk.corpus import wordnet
import random



def convert_intents(intents):
    converted_intents = []
    for intent in intents:
        tag = intent["tag"]
        patterns = "|".join([re.escape(pattern) for pattern in intent["patterns"]])
        responses = intent["responses"]
        converted_intents.append({
            "tag": tag,
            "pattern": re.compile(patterns, re.IGNORECASE),
            "responses": responses
        })
    return converted_intents



def getAnswer(userText, intents):
    converted_intents = convert_intents(intents)
    for intent in converted_intents:
        pattern = intent['pattern']
        tag = intent['tag']
        responses = intent['responses']
        if re.search(pattern, userText):
            return responses[(random.randrange(len(responses)))]
        else:
            return "I cannot understand you"
    