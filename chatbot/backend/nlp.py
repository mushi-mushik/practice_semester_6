import nltk
import random
import string
from nltk.tokenize import word_tokenize

class ChatbotEngine:
    def __init__(self):
        self.intents = {
            "greeting": {
                "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
                "responses": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"]
            },
            "farewell": {
                "patterns": ["bye", "goodbye", "see you", "take care"],
                "responses": ["Goodbye!", "See you later!", "Take care!"]
            },
            "hours_in_day": {
                "patterns": ["how many hours in a day", "hours per day", "day hours"],
                "responses": ["There are 24 hours in a day."]
            },
            "minutes_in_hour": {
                "patterns": ["how many minutes in an hour", "minutes per hour"],
                "responses": ["There are 60 minutes in an hour."]
            },
            "seconds_in_minute": {
                "patterns": ["how many seconds in a minute", "seconds per minute"],
                "responses": ["There are 60 seconds in a minute."]
            },
            "how_are_you": {
                "patterns": ["how are you", "how do you do"],
                "responses": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!"]
            }
        }
        self.fallback_responses = [
            "I'm sorry, I don't understand that.",
            "Could you rephrase that?",
            "I'm not sure how to answer that."
        ]

    def _preprocess(self, text):
        """Tokenize and normalize text."""
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in string.punctuation]
        return tokens

    def get_response(self, user_input):
        """Match user input to an intent and return a response."""
        tokens = self._preprocess(user_input)

        best_intent = None
        best_match_count = 0

        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data["patterns"]:
                pattern_tokens = self._preprocess(pattern)
                match_count = sum(1 for token in pattern_tokens if token in tokens)
                if match_count > best_match_count:
                    best_match_count = match_count
                    best_intent = intent_name

        if best_intent and best_match_count > 0:
            responses = self.intents[best_intent]["responses"]
            return random.choice(responses)
        else:
            return random.choice(self.fallback_responses)

engine = ChatbotEngine()
