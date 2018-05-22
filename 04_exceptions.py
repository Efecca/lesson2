def get_answer(question, answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}):
    try:
        low_question = str(question).lower()
        return answers[low_question]
    except Exception as e:
        return 'Something bad happened'

def ask_user():
    try:
        while True:
            user_say = input('Скажи что-нибудь...')
            if user_say == 'Пока':
                print('Пока!')
                return
            else:
                print(get_answer(user_say))
    except KeyboardInterrupt :
        print("\nНу ты заходи, если что")

ask_user()