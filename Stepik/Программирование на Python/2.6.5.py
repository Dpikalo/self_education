'''
Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
a = int(input())
b = ([[0 for j in range(a)] for i in range(a)])
n = 1
x1 = 0
y1 = 0
for i in range(a//2+1):
  for j in range(x1,a-y1):
    b[i][j] = n
    n +=1
  for j in range(x1+1,a-y1):
    b[j][a-(1+i)] = n
    n +=1
  for j in range(-(2+x1),-(a+1-y1),-1):
    b[a-(1+i)][j] = n
    n +=1
  for j in range(-(2+x1),-(a-y1),-1):
    b[j][i] = n
    n +=1
  x1 += 1
  y1 += 1

for i in range(a):
  for j in range(a):
    print(b[i][j], end=' ')
  print()