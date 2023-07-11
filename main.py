import telebot
from telebot import types
bot = telebot.TeleBot('6143255807:AAGHDgHlVlhrLMvWIHRMgS7qtPV1YqbBRM4')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('амогус')
    but2 = types.KeyboardButton('абобус')
    but3 = types.KeyboardButton('глобус')
    markup.add(but1, but2, but3)

    bot.send_message(message.chat.id, 'здарова', reply_markup=markup)


asdasdasd

bot.polling(none_stop=True)
