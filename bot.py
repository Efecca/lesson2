from datetime import date, timedelta,datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

import ephem
import locale
import re

import calculator
import conversation_calc
import conversation_cities
import settings
import word_count
import word_calculator


# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
date_regex_string = "\d{4}[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])"

def main():
    mybot = Updater(settings.TELEGRAM_API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    #подсчет слов
    dp.add_handler(CommandHandler("wordcount", word_count_command))

    #обычный калькулятор
    dp.add_handler(MessageHandler(Filters.regex('^[1234567890+-/*]+=$'), calc_command))
    #словарный калькулятор
    dp.add_handler(MessageHandler(Filters.regex('^[Сс]колько будет .*'), word_calc_command))
    #полнолуние
    dp.add_handler(MessageHandler(Filters.regex('^[Кк]огда ближайшее полнолуние после {}\?$'.format(date_regex_string)), moon_command))
    #клавиатура
    dp.add_handler(conversation_calc.get_handler_instance())
    #города
    dp.add_handler(conversation_cities.get_handler_instance())

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    #Задание: в функции greet_user выведите на экран содержимое переменной update
    print('Update: {}'.format(update))
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)      


#def talk_to_me(bot, update):

#Добавить команду /wordcount котрая считает сова в присланной фразе. 
#Например на запрос /wordcount "Привет как дела" бот должен посчитать количество слов в кавычках и ответить: 3 слова.
def word_count_command(bot, update):
    text = update.message.text.replace("/wordcount","")
    cnt = word_count.word_count(text)
    print("wordcount {}".format(text))
    update.message.reply_text('Количество слов в этой фразе: {}'.format(str(cnt)))

#Обычный калькулятор 
def calc_command(bot, update):
    user_text = update.message.text 
    res = calculator.calculator(user_text)
    update.message.reply_text(res)

#Словарный калькулятор
def word_calc_command(bot, update):
    user_text = update.message.text 
    res = word_calculator.word_calc(user_text)
    update.message.reply_text(res)

locale.setlocale(locale.LC_ALL, "russian")
def moon_command(bot, update):
    user_text = update.message.text 
    x=re.search(date_regex_string,user_text)
    date_for_check = x.group()
    res = ephem.next_full_moon(date_for_check).datetime()
    update.message.reply_text("Ближайшее полнолуние после {}: {}".format(date_for_check, res.strftime('%d %B %Y %H:%M')))

main()  