from telegram.ext import ConversationHandler, MessageHandler, CommandHandler,Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import calculator

ex_str = ''
SYMBOL = 0

def get_handler_instance():
    return ConversationHandler(
        entry_points=[CommandHandler('addnumpad', add_numpad)],

        states={
            SYMBOL: [MessageHandler(Filters.text, pipe_command)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

def add_numpad(bot, update):
    #print('Update: {}'.format(update))
    chat_id = update.message.chat_id
    custom_keyboard = [['1', '2','3'], 
                      ['4', '5','6'],
                      ['7', '8','9'],
                      ['0', '=','/'],
                      ['+', '-','*']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    bot.sendMessage(chat_id = chat_id , text = 'Done' , reply_markup = reply_markup)

    return SYMBOL

def pipe_command(update, context):
    s = update.message.from_user
    print(s)
    if(s== '='):
        ex_str = ''
        update.message.reply_text('result',
                              reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        ex_str = ex_str+s

        return SYMBOL

def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END