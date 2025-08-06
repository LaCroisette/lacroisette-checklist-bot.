import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! ✅ The bot is working.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
