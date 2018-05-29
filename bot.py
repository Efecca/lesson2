from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import settings
import word_count
import calculator
import word_calculator
import conversation_calc
import conversation_cities

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

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

main()