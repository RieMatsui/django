from django.shortcuts import render
from django.views.generic import TemplateView

from collections import defaultdict


class Dict(TemplateView):

    def __main__(self):
        self.main()

    @staticmethod
    def main():
        print('*' * 5 + '練習25' + '*' * 5)
        d = {'x': 10, 'y': 20}
        print(d)
        print(type(d))
        print(d['x'])
        print(d['y'])
        d['x'] = 100
        print(d)
        d['x'] = 'XXXX'
        print(d)
        d['z'] = 200
        print(d)
        d['1'] = 10000
        print(d)

        print(dict(a=10, b=20))
        print(dict([('a', 10), ('b', 20)]))
        print('*' * 16)

        print('*' * 5 + '練習26' + '*' * 5)
        d = {'x': 10, 'y': 20}
        print(d)

        # 値を取得
        print(d.values())

        # 二つのdict型を上書きする
        d2 = {'x': 1000, 'j': 500}
        d.update(d2)

        # dict型の値を取得
        print(d)
        print(d['x'])
        print(d.get('x'))

        # dict型の値を削除
        r = d.get('z')
        print(type(r))
        d.pop('x')
        print(d)
        del d['y']
        print(d)
        del d
        d = {'a': 100, 'b': 200}
        print(d)
        d.clear()
        print(d)

        d = {'a': 100, 'b': 200}
        has_a = 'a' in d
        print(has_a)
        has_j = 'j' in d
        print(has_j)

        print('*' * 5 + '練習26' + '*' * 5)
        # dict型の複製
        x = {'a': 1}
        y = x
        y['a'] = 1000
        print(x)
        print(y)

        x = {'a': 1}
        y = x.copy()
        y['a'] = 1000
        print(x)
        print(y)

        ranking = {
            "A": 100,
            "B": 85,
            "C":95,
        }
        print(ranking)
        asc_ranking = sorted(ranking, key=ranking.get)
        desc_ranking = sorted(ranking, key=ranking.get, reverse=True)
        print(asc_ranking)
        print(desc_ranking)

        s = "siahciiesideyigeihusui"

        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        print(d)

        d = {}
        for c in s:
            d.setdefault(c, 0)
            d[c] += 1
        print(d)

        d = defaultdict(int)
        for c in s:
            d[c] += 1
        print(d)

        print(d['f'])

    # 練習20
    def get(self, request, *args, **kwargs):
        self.main()
        return render(request, 'practice/dict/index.html')


class PriceCheck(TemplateView):

    # 練習20
    def get(self, request, *args, **kwargs):
        return render(request, 'practice/dict/price_check.html')

    def post(self, request):

        item = {'りんご': 120, 'みかん': 100, 'ぶどう': 500}
        item_price = ''
        item_name = request.POST['item_name']
        if item_name in item:
            item_price = item[item_name]

        context = {
            'item_name': item_name,
            'item_price': item_price,
        }
        return render(request, 'practice/dict/price_check.html', context)
