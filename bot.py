import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("✊✌🤚 Камань, ножницы, бумага")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы развлекать тебя!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == '✊✌🤚 Камань, ножницы, бумага':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("✊ Камень", callback_data='К')
            item2 = types.InlineKeyboardButton("✌️ Ножницы", callback_data='Н')
            item3 = types.InlineKeyboardButton("🤚 Бумага", callback_data='Б')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Выбирай 😁', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'К':
                a = random.randint(1, 3)
                if a == 1:
                    bot.send_message(call.message.chat.id, '✊ Камень')
                    bot.send_message(call.message.chat.id, 'Ничья!')
                elif a == 2:
                    bot.send_message(call.message.chat.id, '✌️ Ножницы')
                    bot.send_message(call.message.chat.id, 'Ты победил!')
                elif a == 3:
                    bot.send_message(call.message.chat.id, '🤚 Бумага')
                    bot.send_message(call.message.chat.id, 'Ты проиграл!')
            elif call.data == 'Н':
                a = random.randint(1, 3)
                if a == 1:
                    bot.send_message(call.message.chat.id, '✊ Камень')
                    bot.send_message(call.message.chat.id, 'Ты проиграл!')
                elif a == 2:
                    bot.send_message(call.message.chat.id, '✌️ Ножницы')
                    bot.send_message(call.message.chat.id, 'Ничья!')
                elif a == 3:
                    bot.send_message(call.message.chat.id, '🤚 Бумага')
                    bot.send_message(call.message.chat.id, 'Ты победил!')
            elif call.data == 'Б':
                a = random.randint(1, 3)
                if a == 1:
                    bot.send_message(call.message.chat.id, '✊ Камень')
                    bot.send_message(call.message.chat.id, 'Ты победил!')
                elif a == 2:
                    bot.send_message(call.message.chat.id, '✌️ Ножницы')
                    bot.send_message(call.message.chat.id, 'Ты проиграл!')
                elif a == 3:
                    bot.send_message(call.message.chat.id, '🤚 Бумага')
                    bot.send_message(call.message.chat.id, 'Ничья!')
            elif call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')


 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
