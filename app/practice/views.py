from django.views.generic import TemplateView
from django.shortcuts import render
import math


class Index(TemplateView):
    # テンプレートファイル連携
    template_name = 'practice/index.html'

    # 変数を渡す
    def get_context_data(self, **kwargs):
        num = 1
        name = 'Mike'
        is_ok = True
        context = super().get_context_data(**kwargs)

        print('*' * 10)
        # 練習8
        context['num'] = num
        print(type(num))
        context['name'] = name
        print(type(name))
        context['is_ok'] = is_ok
        print(type(is_ok))

        # 練習9
        print('Hi', 'Mike', sep=',', end='\n')
        print('Hi', 'Mike', sep=',', end='')
        print('Hi', 'Mike', sep=',', end='.')
        print('*' * 10)

        # 練習10
        context['sqrt'] = math.sqrt(25)
        context['log2'] = math.log2(10)
        # print(help(math))

        # 練習11
        context['helo1'] = 'helo'
        context['helo2'] = "helo"

        context['say1'] = "I don't know"
        context['say2'] = "I don't know"
        context['say3'] = 'say "I don\'t know"'
        context['say4'] = "say \"I don't know\""

        context['say5'] = 'helo.\nHow are you'
        context['dir'] = r'C:\name\name'

        context['line'] = """
        line1
        line2
        line3
        """
        context['hi'] = 'Hi.' * 3 + 'Mike.'
        context['long_string'] = ('aaaaaaaaaaaaaaaaa'
                                  'bbbbbbbbbbbbbbbbb')

        # 練習12
        slice = 'python'
        context['slice1'] = slice[0]
        context['slice2'] = slice[1]
        context['slice3'] = slice[-1]
        context['slice4'] = slice[0:2]
        context['slice5'] = slice[2:5]

        context['slice6'] = slice[0:2]
        context['slice7'] = slice[:2]
        context['slice8'] = slice[2:]
        slice_change = 'j' + slice[1:]
        context['slice9'] = slice_change
        context['slice10'] = slice_change[:]
        context['slice11'] = len(slice_change)

        # 練習13
        text = 'My name is Mike.Hi Mike.'
        context['str_method1'] = text.startswith('My')
        context['str_method2'] = text.startswith('x')

        context['str_method3'] = text.find('Mike')
        context['str_method4'] = text.rfind('Mike')
        context['str_method5'] = text.count('Mike')
        context['str_method6'] = text.capitalize()
        context['str_method7'] = text.title()
        context['str_method8'] = text.upper()
        context['str_method9'] = text.lower()
        context['str_method10'] = text.replace('Mike', 'Nancy')

        # 練習14
        context['str_format1'] = 'a is {}'.format('a')
        context['str_format2'] = 'a is {}'.format('test')
        context['str_format3'] = 'a is {} {} {}'.format(1, 2, 3)
        context['str_format4'] = 'a is {0} {1} {2}'.format(1, 2, 3)
        context['str_format5'] = 'a is {2} {1} {0}'.format(1, 2, 3)
        context['str_format6'] = 'My name is {1} {0}.'.format('Tanaka', 'Taro')
        context['str_format7'] = 'My name is {1} {0}. Watashi ha {0} {1}'.format('Tanaka', 'Taro')
        context['str_format8'] = 'My name is {name} {family}. Watashi ha {family} {name}'. \
            format(family='Tanaka', name='Taro')

        # 練習15
        a = 'a'
        context['str_format9'] = f'a is {a}'

        x, y, z = 1, 2, 3
        context['str_format10'] = f'a is {x}, {y}, {z}'

        name = 'Tanaka'
        family = 'Taro'
        context['str_format11'] = f'My name is {name} {family}. Watashi ha {family} {name}'

        return context


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

    print('*' * 5 + '練習17' + '*' * 5)
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

    print('*' * 5 + '練習17' + '*' * 5)
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


class Seat(TemplateView):

    def get(self, request, *args, **kwargs):

        context = {
            'message': '空席があります',
        }
        return render(request, 'practice/seat.html', context)

    def post(self, request):

        seatStr = ''
        message = '空席があります'
        seat = []

        if self.request.POST.get('seat', None):
            seatStr = request.POST['seat']
            if seatStr.count(',') > 0:
                seat = seatStr.split(',')
            else:
                seat.append(seatStr)

        if self.request.POST.get('input_seat', None):
            input_seat = request.POST['input_seat']
            if 0 <= len(seat) < 5:
                seat.append(input_seat)
                seatStr = ','.join(seat)

        if self.request.POST.get('delete_seat', None):
            delete_seat = request.POST['delete_seat']

            if delete_seat in seat:
                seat.remove(delete_seat)
                seatStr = ','.join(seat)

        if len(seat) == 5:
            message = '空席がありません'

        context = {
            'input_seat': '',
            'delete_seat': '',
            'seat': seatStr,
            'message': message,
        }
        return render(request, 'practice/seat.html', context)


seatView = Seat.as_view()
