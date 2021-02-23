'''
В первой строке даны целое число 1 \le n \le 10^51≤n≤10
5
  и массив A[1 \ldots n]A[1…n] из nn различных натуральных чисел, не превышающих 10^910
9
 , в порядке возрастания, во второй — целое число 1 \le k \le 10^51≤k≤10
5
  и kk натуральных чисел b_1, \ldots, b_kb
1
​
 ,…,b
k
​
 , не превышающих 10^910
9
 . Для каждого ii от 1 до kk необходимо вывести индекс 1 \le j \le n1≤j≤n, для которого A[j]=b_iA[j]=b
i
​
 , или -1−1, если такого jj нет.





Sample Input:

5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:

3 1 -1 1 -1
'''


def search(lst, k):
    l = 0
    l2 = len(lst) - 1
    while l <= l2:
        m = int((l + l2) / 2)
        if lst[m] == k:
            return m + 1
        elif lst[m] > k:
            l2 = m - 1
        else:
            l = m + 1
    return -1


n, *first = map(int, input().split())
k, *second = map(int, input().split())
result = []
for i in range(k):
    a = search(first, second[i])
    result.append(a)
print(*result)
