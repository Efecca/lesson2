numeric_dict = {
    'ноль':'0',
    'один':'1',
    'два':'2',
    'три':'3',
    'четыре':'4',
    'пять':'5',
    'шесть':'6',
    'семь':'7',
    'восемь':'8',
    'девять':'9',
    'десять':'10',
    'точка':'.',
    'плюс':'+',
    'минус':'-',
    'умножить':'*',
    'разделить':'/'
}

#from 10_calc_1 import parse
import calculator
def word_calc(ex_word_str):
    ex_str=''
    for word in ex_word_str.split():
        ex_str = ex_str+numeric_dict.get(word,'')

    return calculator.parse(ex_str)


print('три плюс два={}'.format(str(word_calc("три плюс два"))))
print('шесть минус семь={}'.format(str(word_calc("шесть минус семь"))))
print('шесть минус семь плюс два плюс семь={}'.format(str(word_calc("шесть минус семь плюс два плюс семь"))))
print('шесть точка три плюс два точка семь={}'.format(str(word_calc("шесть точка три плюс два точка семь"))))