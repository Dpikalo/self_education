'''Первая строка содержит количество предметов 1 \le n \le 10^31≤n≤10 3 и вместимость рюкзака 0 \le W \le 2 \cdot
10^60≤W≤2⋅10 6 . Каждая из следующих nn строк задаёт стоимость 0 \le c_i \le 2\cdot 10^60≤c i ​ ≤2⋅10 6 и объём 0 \lt
w_i \le 2\cdot 10^60<w i ​ ≤2⋅10 6 предмета (nn, WW, c_ic i ​ , w_iw i ​ — целые числа). Выведите максимальную
стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом
пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:

3 50
60 20
100 50
120 30
Sample Output:

180.000
'''


def sort_backpack(capacity_backpack, list_items):
    sort_list = [(i / v, v) for i, v in list_items]
    sort_list.sort(reverse=True)
    volume = 0

    for summ, v in sort_list:
        if v < capacity_backpack:
            volume += summ * v
            capacity_backpack -= v
        else:
            volume += summ * capacity_backpack
            break

    return volume


max_items, capacity_backpack = map(int, input().split())
list_items = []
for i in range(max_items):
    list_items.append(tuple(map(int, input().split())))

print('{:.3f}'.format(sort_backpack(capacity_backpack, list_items)))
