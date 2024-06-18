# Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.
file_1 = r'text_1.txt'
file_2 = r'text_2.txt'
with open(file_1, mode='r') as a:
    lst_1 = a.readlines()
with open(file_2, mode='r') as b:
    lst_2 = b.readlines()
diff = []
for i in lst_1:
    if not (i in lst_2):
        diff.append(i)
    for j in lst_2:
        if not j in lst_1:
            diff.append(j)

if len(diff) != 0:
    print('Отличающиеся сторки:')
    for i in diff:
        print(f'{i}\n')
else:
    print('Нет отличающихся строк в обоих файлах!')

# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.
text = r'text_1.txt'
info_text = r'info_text.txt'

with open(text, mode='r') as a:
    lst = a.read()

with open(info_text, mode='w', encoding='utf-8') as f:
    kol_str = lst.count('\n') + 1
    vowels = 'aeiou'
    conson = 'qwrtypsdfghjklzxcvbnm'
    kol_vow = 0
    kol_con = 0
    for letter in lst:
        if letter.lower() in vowels:
            kol_vow += 1
        elif letter.lower() in conson:
            kol_con += 1
    kol_dig = sum(1 for i in lst if i.isdigit())
    f.write(f'Количество символов - {len(lst)}\n'
            f'Количество строк - {kol_str}\n'
            f'Количество гласных букв - {kol_vow}\n'
            f'Количество согласных букв - {kol_con}\n'
            f'Количество цифр - {kol_dig}')

# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.
text_1 = r'text_1.txt'
text_2 = r'text_2.txt'

with open(text_1, mode='r') as f:
    lst = f.readlines()
    del lst[-1]
with open(text_2, mode='w') as a:
    a.writelines(lst)

# Дан текстовый файл. Найти длину самой длинной строки.
text = r'text_1.txt'

with open(text, mode='r') as a:
    lst = a.readlines()
    len_max = len(lst[0])
    maxi = 1
    for i in range(len(lst)):
        if len_max > len(lst[i]):
            len_max = len(lst[i])
            maxi = i + 1
print(f'Самая длиная строка номер {maxi}, её длина - {len_max} символов')

# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.
text = r'text_1.txt'
word = input('Введите слово для поиска в тексте: ')

with open(text, mode='r') as f:
    lst = f.read()
    kol = lst.count(word)

print(f'Слово "{word}" встречается в тексте {kol} раз')

# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.
text = r'text_1.txt'
word_find = input('Введите слово для поиска в тексте: ')
word_replace = input('Введите слово для замены в тексте: ')

with open(text, mode='r') as f:
    lst = f.read()
    lst = lst.replace(word_find, word_replace)

with open(text, mode='w') as a:
    a.write(lst)
