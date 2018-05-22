#Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". 
#Когда найдете напишите "Валера нашелся". 
#Подсказка: используйте метод list.pop()
names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while True:
    name = names.pop()
    if name == 'Валера':
        print('Валера нашелся')
        break

#Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
#Это просто какая-то боль
def find_person(name):
    for current_name in names:
        if name == current_name:
            return True
    return False

#Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
def ask_user():
    while True:
        user_say = input('Как дела?')
        if user_say == 'Хорошо':
            print('Ну и отлично')
            return

#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
#get_answer() в другом файле, но импортирование только в следующем письме, так что ничего не поделаешь
def get_answer(question, answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}):
    try:
        low_question = str(question).lower()
        return answers[low_question]
    except Exception as e:
        return 'Something bad happened'

def ask_user():
    while True:
        user_say = input('Скажи что-нибудь...')
        if user_say == 'Пока':
            print('Пока!')
            return
        else:
            print(get_answer(user_say))