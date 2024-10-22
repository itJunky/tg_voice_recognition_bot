import telebot
import time
from common import recognize
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(msg):
    bot.reply_to(msg, """\
Здравствуй, дорогой друг. Я расскажу тебе сказочку на ночь.
""" )

#@bot.message_handler(func=lambda message: True, content_types=['audio', 'voice', 'video'])
@bot.message_handler(content_types=['audio', 'voice', 'video', 'video_note'])
def media_recognize(message):
    print(message)
    try:
        file_id = message.voice.file_id
    except AttributeError:
        try:
            file_id = message.video.file_id
        except AttributeError:
            try:
                file_id = message.video_note.file_id
            except AttributeError:
                try:
                    file_id = message.audio.file_id
                except Exception as e:
                    print(e)

    url = bot.get_file(file_id)
    print(url)
    downloaded_file = bot.download_file(url.file_path)
    tmp_file_name = str(time.time()) + '.oga'
    with open(tmp_file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    res = recognize(tmp_file_name)
    print(res)
    bot.reply_to(message, res)
    # TODO remove file and text after send

bot.infinity_polling()

