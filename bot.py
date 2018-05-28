from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import settings
import word_count
import calculator
import word_calculator
import conversation_calc

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
    
    #custom_keyboard = [['top-left', 'top-right'], 
    #                  ['bottom-left', 'bottom-right']]
    #reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    #mybot.send_message(chat_id=chat_id, 
    #                  text="Custom Keyboard Test",  
    #                  reply_markup=reply_markup)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count_command))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.regex('^[1234567890+-/*]+=$'), calc_command))
    dp.add_handler(MessageHandler(Filters.regex('^[Сс]колько будет .*'), word_calc_command))
    dp.add_handler(MessageHandler(Filters.regex('^[Сс]колько будет .*'), word_calc_command))

    dp.add_handler(conversation_calc.get_handler_instance())

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    #Задание: в функции greet_user выведите на экран содержимое переменной update
    print('Update: {}'.format(update))
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)      


def talk_to_me(bot, update):
    update.message.reply_text("кастомная клавиатура")
    custom_keyboard = [['top-left', 'top-right'], 
                      ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    update.message.reply_text("кастомная клавиатура - 2",  
                      reply_markup=reply_markup)

 
def calc_command(bot, update):
    user_text = update.message.text 
    res = calculator.calculator(user_text)
    update.message.reply_text(res)

def word_calc_command(bot, update):
    user_text = update.message.text 
    res = word_calculator.word_calc(user_text)
    update.message.reply_text(res)

#Добавить команду /wordcount котрая считает сова в присланной фразе. 
#Например на запрос /wordcount "Привет как дела" бот должен посчитать количество слов в кавычках и ответить: 3 слова.
def word_count_command(bot, update):
    text = update.message.text.replace("/wordcount","")
    cnt = word_count.word_count(text)
    print("wordcount {}".format(text))
    update.message.reply_text('Количество слов в этой фразе: {}'.format(str(cnt)))

main()