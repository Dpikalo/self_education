'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''
with open("file_input.txt") as inp, open("file_output.txt", "w") as out:
    for line in list(reversed(list(inp))):
        out.write(line)