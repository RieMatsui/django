from django.views.generic import TemplateView
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