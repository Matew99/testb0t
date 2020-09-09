import telebot
import emoji
from telebot import types

bot = telebot.TeleBot('1101142811:AAEecaC-3zetabA3_iE9hW21AQ-CLqFm7hU')

@bot.message_handler(commands=['crazy'])
def crazy(message):
    send_mess = f"*{message.from_user.first_name}*, да ты крейзи"+emoji.emojize(":thumbs_up:")
    bot.send_message(message.chat.id, send_mess, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('КАЛАБАНГА'+emoji.emojize(":thumbs_up:"))
    btn2 = types.KeyboardButton('ФЛАМИНГО')
    btn3 = types.KeyboardButton('МАЗАФАКА')
    btn4 = types.KeyboardButton('Часто задаваемые вопросы')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"*Привет {message.from_user.first_name}*\nЧто тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, "Ваша ссылка: (https://konoplisemena.com)", parse_mode='Markdown')


bot.polling(none_stop=True)
