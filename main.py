from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TELEGRAM_BOT_TOKEN
from handlers import handle_message

def start(update, context):
    update.message.reply_text("Hello! I'm a crypto AI bot. How can I help?")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
