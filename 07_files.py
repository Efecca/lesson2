words = 0
with open('referat.txt', 'r', encoding='utf-8') as f:
    words += sum(sum(w !='' and w !='\n'  for w in line.split(' ')) for line in f)

print('Число слов в файле: {}'.format(str(words)))