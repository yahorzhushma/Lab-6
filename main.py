import telebot
from telebot import types

bot = telebot.TeleBot('6786101341:AAG03-QppB_BaRggZsDC5jdrfwxtpn903RY')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    reg = types.KeyboardButton('Регистрация')
    sched = types.KeyboardButton('Расписание')
    spkrs = types.KeyboardButton('Спикеры')
    merch = types.KeyboardButton('Мерч')
    loc = types.KeyboardButton('Как добраться?')
    markup.row(reg)
    markup.row(loc)
    markup.row(sched, spkrs)
    markup.row(merch)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Регистрация':
        bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSdPyv7s8JTl6soLe1KCBbs9NlhE8qQVBBjBJTsQT91GTby7TQ/closedform')
    elif message.text == "Расписание":

    elif message.text == "Спикеры":
    elif message.text == "Мерч":
    elif message.text == "Как добраться?":
        bot.send_location(1046586658, 53.878056, 27.490880)


bot.polling(none_stop=True)
