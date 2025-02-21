import re
from telegram import Update
from telegram.ext import CallbackContext
from utils import detect_emotion, detect_topic
from response_generator import generate_response

def handle_message(update: Update, context: CallbackContext):
    """Handles incoming messages and generates responses."""
    user_message = update.message.text.lower()

    emotion = detect_emotion(user_message)
    topic = detect_topic(user_message)
    response = generate_response(user_message, topic, emotion)

    update.message.reply_text(response)
