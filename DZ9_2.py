import telebot
from telebot import types

bot = telebot.TeleBot('5998676166:AAGNZVGAfoZSZFiaGcGd1NkfgPiGGmQpVHg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else:
        bot.send_message(message.from_user.id, "Для начала работы напиши Привет")
    
bot.polling(none_stop=True, interval=0)


    