'''
По данным nn отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1 \le n \le 1001≤n≤100 отрезков. Каждая из последующих nn строк содержит по два числа 0 \le l \le r \le 10^90≤l≤r≤10
9
 , задающих начало и конец отрезка. Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:

3
1 3
2 5
3 6
Sample Output 1:

1
3
Sample Input 2:

4
4 7
1 3
2 5
5 6
Sample Output 2:

2
3 6
'''


def res(list_res):
    resulting_list_res = []
    while len(list_res) > 0:
        if len(list_res) < 2:
            turf = list_res.pop()
            resulting_list_res.append(turf)
        else:
            a, b = list_res[0], list_res[1]
            if b[0] <= a[1]:
                left, right = b[0], b[1] if b[1] <= a[1] else a[1]
                overlapping = (left, right)
                list_res = list_res[2:]
                list_res = [overlapping] + list_res
            else:
                resulting_list_res.append(list_res[0])
                list_res = list_res[1:]
    return [i[1] for i in resulting_list_res]


n = int(input())
list_res = []
for i in range(n):
    list_res.append(tuple(map(int, input().split())))
list_res.sort(key=lambda x: (x[0], x[1]))
result = res(list_res)
print(len(result))
print(*result)
