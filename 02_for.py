#Создать список из десяти целых чисел.
#Вывести на экран каждое число, увеличенное на 1.
test_list = list(range(10))
print(', '.join(str(i+1) for i in test_list))

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.
test_string = input('enter test_string: ')
print('\n'.join(s for s in test_string))

import random
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
grades_list = []
letters='abcdefgh'
for i in range(random.randint(1,10)):
    var = {'school_class': '{}{}'.format(str(random.randint(1,11)), random.choice(letters))}
    var['scores'] = [random.randint(1,5) for j in range(random.randint(20,30))]
    grades_list.append(var)
print(grades_list)
# Посчитать и вывести средний балл по всей школе.
avg_grage = sum([sum(cl['scores']) for cl in grades_list])/sum([len(cl['scores']) for cl in grades_list])
print('Cредний балл по всей школе: {}'.format(avg_grage))
# Посчитать и вывести средний балл по каждому классу.
print('\n'.join('Cредний балл по классу {}: {}'.format(cl['school_class'], str(sum(cl['scores'])/len(cl['scores']))) for cl in grades_list))