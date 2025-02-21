Telegram AI Bot 🤖💬

This is a modular AI chatbot designed for Telegram using Cohere AI. The bot detects sentiment, topics, and engages users with humor and wit.

🚀 Features

🔍 Detects emotions (positive, neutral, negative)

💡 Topic detection (e.g., project updates, hype, general chat)

🤖 AI-powered responses via Cohere

⚡ Customizable prompts

🔒 Secure API key storage (via .env)

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/telegram-ai-bot.git
cd telegram-ai-bot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure API Keys

Create a .env file (copy .env.example and rename it to .env).

Add your API keys:

TELEGRAM_BOT_TOKEN=your-telegram-bot-token
COHERE_API_KEY=your-cohere-api-key
BOT_NAME=YourBotName

4️⃣ Run the Bot

python bot/main.py

📌 Customization

Change the bot’s personality in prompts.py

Modify topic detection in handlers.py

🤝 Contributing

Pull requests are welcome! Feel free to submit improvements or bug fixes.

📜 License

This project is private. Do not redistribute without permission.
