'''По данному числу 1 \le n \le 10^91≤n≤10 9 найдите максимальное число kk, для которого nn можно представить как
сумму kk различных натуральных слагаемых. Выведите в первой строке число kk, во второй — kk слагаемых.

Sample Input 1:

4
Sample Output 1:

2
1 3
Sample Input 2:

6
Sample Output 2:

3
1 2 3
'''


def sort(n):
    res = []
    a, b = 1, n - 1
    while b > a:
        res.append(a)
        a += 1
        b = b - a
    res.append(n - sum(res))
    return res


result = sort(int(input()))
print(len(result))
print(*result)
