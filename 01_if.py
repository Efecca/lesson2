#Возраст
#Попросить пользователя ввести возраст.
age_string = input("Введите возраст: ")
try:
    age = float(age_string)
    #По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
    # Вывести занятие на экран.
    if age < 0 or age > 111:
        print("Не-не-не, Девид Блейн, не-не-не")
    elif age<18: #понятия не имею, до скольки нынче учатся.
        print("Школа" if age >= 7 else "Детский сад")
    else:
        print("Работа" if age >= 24 else "ВУЗ")
except ValueError:
    print("Нужен был возраст в числах")

# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
def string_comparator(s1,s2):
# Если строки одинаковые, возвращает 1.
    if s1==s2:
        return 1
# Если строки разные и первая длиннее, возвращает 2.
    elif len(s1) > len(s2):
        return 2
# Если строки разные и вторая строка 'learn', возвращает 3.
    elif s2=='learn':
        return 3
#should be 1        
print('Should be 1: {} '.format(string_comparator('s1','s1')))
#should be 2
print('Should be 2: {} '.format(string_comparator('s111','s2')))
#should be 3
print('Should be 3: {} '.format(string_comparator('s1','learn')))
#I have no idea, what should be here. In C# - compiler error in function definition.
print('I have no idea, what should be here. In C# - compiler error in function definition: {} '.format(string_comparator('s1','s2')))