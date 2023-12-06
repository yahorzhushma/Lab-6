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
    pray_rooms = types.KeyboardButton('Молитвенные комнаты')
    loc = types.KeyboardButton('Как добраться?')
    markup.row(reg)
    markup.row(loc)
    markup.row(sched, spkrs)
    markup.row(merch)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def send_multiple_images(chat_id, images):
    media = []
    for img in images:
        photo = telebot.types.InputMediaPhoto(open(img, 'rb'))
        media.append(photo)
    bot.send_media_group(chat_id, media)

def on_click(message):
    if message.text == 'Регистрация':
        bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSdPyv7s8JTl6soLe1KCBbs9NlhE8qQVBBjBJTsQT91GTby7TQ/closedform')
        bot.send_message(message.chat.id, 'Несколько уточнений:\n🔹 Регистрация для участия в конференции обязательна (минимальный возраст: 17+);\n🔹 Регистрационный взнос - 10р. (с питанием, 3 приёма пищи - 30р.), необходимо внести заблаговременно, до конференции! Это можно сделать после каждого молодёжного и воскресного собрания, в 504 аудитории, начиная с 20 октября;\n\n🔸 Если ты не имеешь финансовой возможности внести рег. взнос, укажи это при регистрации;\n🔸 Если у тебя есть желание оплатить регистрацию человека, который не имеет финансовой возможности покрыть расходы самостоятельно, ты также сможешь это указать при регистрации (в случае необходимости с тобой свяжутся).')
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Расписание":
        schedule_photo = open('schedule.jpg', 'rb')
        bot.send_photo(message.chat.id, schedule_photo)
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Спикеры":
        images = ['speaker1.jpg', 'speaker2.jpg']
        send_multiple_images(message.chat.id, images)
        bot.send_message(message.chat.id, 'Пора знакомиться!\nСпикер первого дня конференции Шаг Веры "Чтобы найтись в Нём" - БОРЕЙКО АНДРЕЙ 🔥\n\n- пастор церкви "Христос для народов" (ХДН) ⛪️\n- муж, отец 3-их детей 😍\n- важное утверждение жизни: «У ВСЕГО ЕСТЬ ПРОЦЕСС» 💡\n\nПастор Андрей будет делиться посланием 6 ноября на служении в 17.00 🤍\n\n\nТакже рады представить Вам спикера второго дня конференции Шаг Веры "Чтобы найтись в Нём" - АНДРОНОВИЧ ВАСИЛИЙ 🔥\n\n- пастор церкви ХВЕ в г.Иваново ⛪️\n- бакалавр христианского служения 📖\n- муж, отец 3-их сыновей 😍\n- важный жизненный тезис: «В главном - единство, во второстепенном - свобода, во всём - любовь» 💡\n\nПастор Василий поделится серией посланий 7 ноября на сессиях в 12.00 и 14:30 🌿')
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Мерч":
        images = ['merch1.jpg', 'merch2.jpg', 'merch3.jpg', 'merch4.jpg', 'merch5.jpg', 'merch6.jpg', 'merch7.jpg']
        send_multiple_images(message.chat.id, images)
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Как добраться?":
        bot.send_location(1046586658, 53.878056, 27.490880)
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
