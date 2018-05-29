from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, RegexHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import json
import calculator
import logging
import random
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CITY, CHOICE = range(2)

def get_handler_instance():
    return ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(re.compile('^Сыграем в города\?$',flags=re.IGNORECASE)), cities_start)],

        states={
            CITY: [MessageHandler(Filters.regex('^[Сс]даюсь$'), give_up),
                   MessageHandler(Filters.text, new_city, pass_user_data=True),
                   CommandHandler('hint', hint, pass_user_data=True),
                   CommandHandler('giveup', give_up),],

            CHOICE:[MessageHandler(Filters.regex('(Ты|Я)'), choice, pass_user_data=True)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

def cities_start(bot, update):
    custom_keyboard = [['Ты', 'Я']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Хорошо, кто начинает?',reply_markup=ReplyKeyboardMarkup(custom_keyboard))

    return CHOICE

def choice(bot, update, user_data):
    res = update.message.text
    with open('cities.json', encoding="utf8") as f:
        load_data = json.load(f)
    #что-то тут не то с параметрами, но работает только так
    user_data["cities"] = load_data["cities"]
    user_data["used"] = []
    user_data["index"]={}
    user_data["hints"]=10

    construct_index(user_data)

    if res == 'Я':
         update.message.reply_text('Ок, давай', reply_markup=ReplyKeyboardRemove())
    else :
        val = random.choice(user_data['cities'])
        add_to_used(user_data,val)
        update.message.reply_text(val, reply_markup=ReplyKeyboardRemove())

    return CITY

def new_city(bot, update, user_data):
    user_city = update.message.text

    if user_data['cities']:
        #Здесь регистрозависимый поиск, ну упс
        if user_city not in user_data['cities']:
            update.message.reply_text("Нет такого города {}, давай еще раз".format(user_city))
            return CITY

        if user_data['used']:
            prev_city = user_data['used'][-1]
            prev_letter = get_last_letter(prev_city)
            if not user_city.lower().startswith(prev_letter):
                update.message.reply_text("Не-не-не, так нехорошо {} не на букву {} из {}".format(user_city, prev_letter, prev_city))
                return CITY

        if user_city in user_data['used']:
            update.message.reply_text("Этот город уже был {}, давай другой".format(user_city))
            return CITY

        add_to_used(user_data,user_city)
        city = get_city(user_data,user_city)
        update.message.reply_text(city)
        return CITY

    else:
        update.message.reply_text("Ты выиграл!")
        return ConversationHandler.END

    return CITY

def hint(bot, update, user_data):
    if not user_data['used']:
        return random.choice(user_data['cities'])

    if user_data['hints'] == 0:
        update.message.reply_text('Все подсказки кончились!')
    else:
        user_data['hints']-=1
        print(user_data['hints'])
        prev_city = user_data['used'][-1]
        hint_city = get_next_city(user_data, prev_city)
        if hint_city == '':
            update.message.reply_text('Я выиграл! Больше нет городов на {}'.format(get_last_letter(prev_city)))
            return ConversationHandler.END
        else:
            update.message.reply_text(hint_city)

    return CITY

def give_up(bot, update):
    update.message.reply_text('Так-то!')
    return ConversationHandler.END

def cancel(bot, update):
    update.message.reply_text('Игра отменена',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def add_to_used(user_data,val):
    user_data["used"].append(val)
    user_data["index"][val[0].lower()].remove(val)

def get_next_city(user_data, user_city):
    letter = get_last_letter(user_city)
    print('letter {}, user_city {}'.format(letter, user_city))
    city=''
    variants = user_data["index"].get(letter,[])
    if variants:
        city = random.choice(variants)

    return city

def get_city(user_data, user_city):
    city = get_next_city(user_data, user_city);
    if city == '':
        update.message.reply_text('Ты выиграл!')
        return ConversationHandler.END

    add_to_used(user_data,city)

    return city

def get_last_letter(val):
    excluded_symbols = ['ъ','ь','ы']
    #в общем случае неверно, но пока сойдет
    return val[-1] if val[-1] not in excluded_symbols else val[-2]

#Сложно сказать, зачем здесь индекс на таких-то данных,
#но мое чувство прекрасного требует
def construct_index(user_data):
    for city in user_data["cities"]:
        symbol = city[0].lower()
        if(symbol not in user_data["index"]):
            user_data["index"][symbol] = []

        user_data["index"][symbol].append(city)
