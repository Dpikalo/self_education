'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу. Если
ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет,
то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''


def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key is not d:
        if 2 * key is d:
            d[2 * key].append(value)
        elif (2 * key is not d) and d.get(2 * key) == None:
            d[2 * key] = []
            d[2 * key].append(value)
        elif (2 * key is not d) and d.get(2 * key) != None:
            d[2 * key].append(value)
    return
