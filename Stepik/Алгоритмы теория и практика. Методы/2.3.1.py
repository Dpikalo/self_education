'''
Даны целые числа 1 \le n \le 10^{18}1≤n≤10
18
  и 2 \le m \le 10^52≤m≤10
5
 , необходимо найти остаток от деления nn-го числа Фибоначчи на mm.





Sample Input:

10 2
Sample Output:

1
'''


def fib_mod(n, m):
    n_2 = 0
    n_1 = 1
    mass = [n_2, n_1]

    for curr in range(1, n):
        fibOld = n_1
        n_1, n_2 = (n_1 + n_2) % m, fibOld

        if n_2 == 0 and n_1 == 1:
            mass.pop()
            break
        else:
            mass.append(n_1)
    return mass[n % len(mass)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()