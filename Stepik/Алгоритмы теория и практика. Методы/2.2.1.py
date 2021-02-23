'''
Дано целое число 1 \le n \le 401≤n≤40, необходимо вычислить nn-е число Фибоначчи (напомним, что F_0=0F
0
​
 =0, F_1=1F
1
​
 =1 и F_n=F_{n-1}+F_{n-2}F
n
​
 =F
n−1
​
 +F
n−2
​
  при n \ge 2n≥2).

Sample Input:

3
Sample Output:

2
'''


def fib(n):
    a = 0
    if n == 0:
        return 0
    n_2 = 0
    n_1 = 1
    if n == 1:
        return n_1
    for i in range(n - 1):
        a = n_1 + n_2
        n_1, n_2 = a, n_1
    return a


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
