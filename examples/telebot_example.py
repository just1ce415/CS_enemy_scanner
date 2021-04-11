import telebot
from telebot import types
from random import randint
from datetime import date

bot = telebot.TeleBot("YOUR_TOKEN")

today = date.today()

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("Generate random horoscope")
    button_2 = types.KeyboardButton(f"Choose a horoscope for {today}")

    markup.add(button_1, button_2)

    bot.send_message(message.chat.id, "Hi {0.first_name}!\n\
    I'm bot, choose a number!"
                     .format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    nums_lst = ['1', '2', '3', '4']

    if message.chat.type == 'private':
        if message.text == "Generate random horoscope":
            bot.send_message(message.chat.id, nums_lst[randint(0, 11)])
        elif message.text == f"Choose a horoscope for {today}":

            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton('1', callback_data="01")
            button2 = types.InlineKeyboardButton('2', callback_data="02")
            button3 = types.InlineKeyboardButton(
                '3', callback_data="03")
            button4 = types.InlineKeyboardButton(
                '4', callback_data="04")

            markup.add(button1, button2, button3, button4)

            bot.send_message(message.chat.id, "Choose", reply_markup=markup)

        else:
            bot.send_message(
                message.chat.id, "Ops, I don't know what to answer...")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == "01":
                bot.send_message(
                    call.message.chat.id, "Your num = 1")
            elif call.data == "02":
                bot.send_message(
                    call.message.chat.id, "Your num = 2")
            elif call.data == "03":
                bot.send_message(
                    call.message.chat.id, "Your num = 3")
            elif call.data == "04":
                bot.send_message(
                    call.message.chat.id, "Your num = 4")

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Choose your zodiac sign, please", reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
