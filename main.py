import telebot
from os import environ, makedirs
from dotenv import load_dotenv
from utils.logger import logger

makedirs("output", exist_ok=True)

load_dotenv(".env")

TOKEN = environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


logger.info("=== Bot started ===")
bot.polling()
