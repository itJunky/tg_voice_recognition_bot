import telebot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(msg):
    bot.reply_to(msg, """\
Здравствуй, дорогой друг. Я расскажу тебе сказочку на ночь.
""" )

bot.infinity_polling()

