
import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('<token_from_BotFather>')


@bot.message_handler(commands=['start'])
def start(message):
    bot.delete_message(message.chat.id, message.message_id)

    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT name, response FROM content')
    queryset = cursor.fetchall()
    connection.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for item in queryset[1:]:
        button = types.KeyboardButton(text=f'{item[0]}')
        markup.add(button)

    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!', parse_mode='html')
    bot.send_message(message.chat.id, queryset[0][1], parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_content(message):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute(f"SELECT response FROM content WHERE name='{message.text}'")
    response = cursor.fetchall()
    connection.close()
    bot.send_message(message.chat.id, response, parse_mode='html')


bot.infinity_polling()
