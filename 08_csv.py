import csv
answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
with open('answers.csv', 'w', encoding='utf-8') as f:
    fields = ['answer', 'reply']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for key,value in answers.items():
        writer.writerow({'answer':key, 'reply':value})