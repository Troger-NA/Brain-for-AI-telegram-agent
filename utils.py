import re
from textblob import TextBlob
from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("text-classification", model="distilbert-base-uncased", return_all_scores=True)

def detect_emotion(text):
    """Detects emotion using BERT and TextBlob sentiment analysis."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    bert_scores = classifier(text)[0]

    bert_positive = next((score for score in bert_scores if score['label'] == 'LABEL_1'), {'score': 0.0})['score']
    bert_negative = next((score for score in bert_scores if score['label'] == 'LABEL_0'), {'score': 0.0})['score']

    if polarity > 0.1 or bert_positive > 0.6:
        return "positive"
    elif polarity < -0.1 or bert_negative > 0.6:
        return "negative"
    return "neutral"

def detect_topic(user_message, keywords, context_keywords):
    """Detects the topic of the user message using regex patterns and keyword matching."""
    user_message_lower = user_message.lower()

    # Regex pattern matching
    for category, patterns in keywords.items():
        for pattern in patterns:
            if re.search(pattern, user_message_lower):
                return category

    # Contextual keyword matching
    for category, keywords_list in context_keywords.items():
        if any(keyword in user_message_lower for keyword in keywords_list):
            return category

    return "general"  # Default topic if no match is found

def truncate_to_complete_sentence(text, max_length):
    """Truncates text to the last complete sentence within the max length."""
    if len(text) <= max_length:
        return text

    truncated_text = text[:max_length]
    match = re.search(r'([.!?])[^.!?]*$', truncated_text)

    if match:
        return truncated_text[:match.end()].strip()
    
    return truncated_text.strip()
