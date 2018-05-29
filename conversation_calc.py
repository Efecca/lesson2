from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, RegexHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import calculator
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

SYMBOL = 0

def get_handler_instance():
    return ConversationHandler(
        entry_points=[CommandHandler('addnumpad', add_numpad, pass_user_data=True)],

        states={
            SYMBOL: [MessageHandler(Filters.text, pipe_command, pass_user_data=True)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

def add_numpad(bot, update, user_data):
    custom_keyboard = [['1', '2','3'], 
                      ['4', '5','6'],
                      ['7', '8','9'],
                      ['0', '=','/'],
                      ['+', '-','*']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Done',reply_markup=ReplyKeyboardMarkup(custom_keyboard))
    
    if('ex_str' not in user_data):
        user_data['ex_str'] = ''

    user_data["test"] = "test"
    return SYMBOL

def pipe_command(bot, update,user_data):
    s =  update.message.text
    print(user_data)
    if(s == '='):
        res = calculator.calculator(user_data['ex_str']+'=') 
        update.message.reply_text(res,
                              reply_markup=ReplyKeyboardRemove())
        user_data['ex_str'] = ''

        return ConversationHandler.END
    else:
        user_data['ex_str'] = user_data['ex_str']+s

    return SYMBOL

def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Calculation cancelled',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END