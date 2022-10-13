from django.views.generic import TemplateView
from django.shortcuts import render


class List(TemplateView):
    # テンプレートファイル連携
    template_name = 'practice/list.html'

    print('*' * 5 + '練習16' + '*' * 5)
    list_1 = [1, 20, 4, 50, 2, 1, 2]
    print(list_1[0])
    print(list_1[1])
    print(list_1[-1])
    print(list_1[-2])
    print(list_1[0:2])
    print(list_1[:2])
    print(list_1[2:5])
    print(list_1[2:])
    print(list_1[:])

    print(len(list_1))
    print(type(list_1))

    print('-----------------')

    list_2 = list('abcdefg')
    print(list_2)

    print('-----------------')

    list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_3)
    print(list_3[::2])
    print(list_3[::-1])

    print('-----------------')
    nest_list_1 = ['a', 'b', 'c']
    nest_list_2 = [1, 2, 3]
    nest_list_3 = [nest_list_1, nest_list_2]
    print(nest_list_3)
    print(nest_list_3[0])
    print(nest_list_3[1])
    print(nest_list_3[0][1])
    print(nest_list_3[1][2])
    print('*' * 16 + '\n')

    print('*' * 5 + '練習17' + '*' * 5)
    print('#リストの取り出し')
    list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    print(list_1)
    print(list_1[0])

    list_1[0] = 'x'
    print(list_1)
    print(list_1[2:5])

    list_1[2:5] = ['C', 'D', 'E']
    print(list_1)

    list_1[2:5] = []
    print(list_1)
    print(list_1[:])
    list_1[:] = []
    print(list_1)

    print('-----------------')
    print('#リストの追加')
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_2)
    list_2.append(100)
    print(list_2)
    list_2.insert(0, 200)
    print(list_2)
    list_2.pop()
    print(list_2)
    list_2.pop(0)
    print(list_2)
    print('-----------------')

    print('#リストの削除')
    del list_2[0]
    print(list_2)
    del list_2

    list_2 = [1, 2, 2, 2, 3]
    list_2.remove(2)
    print(list_2)
    list_2.remove(2)
    list_2.remove(2)
    print(list_2)

    print('-----------------')
    print('#リストの結合')
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [6, 7, 8, 9, 10]
    list_3 = list_1 + list_2
    print(list_3)
    list_1 += list_2
    print(list_1)

    list_x = [1, 2, 3, 4, 5]
    list_y = [6, 7, 8, 9, 10]
    list_x.extend(list_y)
    print(list_x)
    print('*' * 16)

    print('*' * 5 + '練習18' + '*' * 5)
    r = [1, 2, 3, 4, 1, 2, 3]
    print(r.index(3))
    print(r.index(3, 3))
    print(r.count(3))
    if 3 in r:
        print('exist')

    elif 100 in r:
        print('exist')

    r.sort()
    print(r)

    r.sort(reverse=True)
    print(r)

    r.reverse()
    print(r)

    s = 'My name is Mike.'
    to_split = s.split(' ')
    print(to_split)

    x = ','.join(to_split)
    print(x)

    print('*' * 16)

    print('*' * 5 + '練習19' + '*' * 5)
    i = [1, 2, 3, 4, 5]
    j = i
    j[0] = 100
    print('j =', j)
    print('j =', i)

    print('-----------------')
    i = [1, 2, 3, 4, 5]
    j = i.copy()
    j[0] = 100
    print('j =', j)
    print('j =', i)

    print('-----------------')
    i = [1, 2, 3, 4, 5]
    j = i[:]
    j[0] = 100
    print('j =', j)
    print('j =', i)

    print('-----------------')
    X = 20
    Y = x
    print(id(X))
    print(id(Y))
    print(X)
    print(Y)
    print('-----------------')
    X = ['a', 'b']
    Y = X
    Y[0] = 'p'
    print(id(X))
    print(id(Y))
    print(X)
    print(Y)
    print('*' * 16)