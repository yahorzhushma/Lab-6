import telebot

bot = telebot.TeleBot('6786101341:AAG03-QppB_BaRggZsDC5jdrfwxtpn903RY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='')


@bot.message_handler()
def get_user_text(message):
    if message.text == "location":
        bot.send_location(1046586658, 53.878056, 27.490880)


bot.polling(none_stop=True)
