import telebot
from telebot import types
from parsing import statistics_mistermax
from parsing import get_semei_weather
from parsing import newskz
bot = telebot.TeleBot(token='6445909231:AAGzqcYs3-GnJOsdqE4jOOX6euirA6ubH4E')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    welcome_message = 'Приветствую, меня звать BotMother! Чем могу помочь?'
    available_commands = '/start - Начать\n/help - Помощь'
    bot.send_message(user_id, welcome_message + available_commands)

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = "Выберите действие:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton ("Узнать новости")
    button2 = types.KeyboardButton("Узнать погоду")
    button3 = types.KeyboardButton ("Узнать статистику Мистера Макса")
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(user_id, help_text, reply_markup = markup)

@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    user_id = message.chat.id
    text = message.text

    if str(text).lower() == 'привет':
        bot.send_message(user_id, 'Здравствуйте!')
    elif str(text).lower() == 'узнать погоду':
        bot.send_message(user_id, get_semei_weather())
    elif str(text).lower() == 'узнать статистику мистера макса':
        bot.send_message(user_id, statistics_mistermax())
    elif str(text).lower() == 'узнать новости':
        bot.send_message(user_id, newskz())
    else:
        bot.send_message(user_id, 'Амир взял всё с ChatGPT!')

bot.polling(none_stop=True)