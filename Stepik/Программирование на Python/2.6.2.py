'''Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется
столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов
последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел
в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

Sample Input:

7
Sample Output:

1 2 2 3 3 3 4
'''
a = int(input())
sum = 0
now = 0
sumn = 0
for i in range(1,a+1):
  now = i
  if sumn == a:
        break
  while now != sum:
    print(now,end = ' ')
    sum += 1
    sumn +=1
    if sumn == a:
        break
  sum = 0