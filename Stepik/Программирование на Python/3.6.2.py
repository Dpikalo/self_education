'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
import requests
f = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while 'We' not in f.text:
    f = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{f.text}')
print(f.text)