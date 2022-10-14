from django.views.generic import TemplateView
from django.shortcuts import render


class Tuple(TemplateView):
    print('*' * 5 + '練習20' + '*' * 5)
    t = (1, 2, 3, 4, 1, 2)
    print(type(t))
    print(t[0])
    print(t[2:5])
    print(t.index(1))
    print(t.index(1, 1))
    print(t.count(1))
    print('*' * 16)

    t = ([1, 2, 3], [4, 5, 6])
    print(t[0][0])
    t = 1, 2, 3
    print(type(t))
    t = 1,
    print(type(t))
    t = ()
    print(type(t))
    t = (1)
    print(type(t))
    t = (1,)
    print(type(t))

    new_tuple = (1, 2, 3) + (4, 5, 6)
    print(new_tuple)
    new_tuple = (1,) + (4, 5, 6)
    print(new_tuple)

    print('*' * 5 + '練習21' + '*' * 5)

    num_tuple = (10, 10)
    print(num_tuple)

    x, y = num_tuple
    print(x, y)

    x, y = 10, 20
    print(x, y)

    min, max = 0, 100
    print(min, max)

    a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
    print(a, b, c, d, e, f)
    a = 'Mike'
    b = '1'

    print('*' * 16)
    i = 10
    j = 20
    tmp = i
    i = j
    j = tmp
    print(i, j)

    a = 100
    b = 200
    print(a, b)
    a, b = b, a
    print(a, b)

    def get(self, request, *args, **kwargs):
        # テンプレートファイル連携
        template_name = 'practice/tuple.html'

        chose_from_two = ('A：漫画', 'B：アニメ', 'C：どちらでもない')

        context = {
            'chose_from_two': chose_from_two,
            'question': '漫画とアニメどちらが好きですか',
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'practice/tuple.html'

        chose_from_two = ('A：漫画', 'B：アニメ', 'C：どちらでもない')
        context = {
            'chose_from_two': chose_from_two,
            'question': '漫画とアニメどちらが好きですか',
            # TODO データベースに登録する
            'answer': request.POST['answer'],
        }
        return render(request, template_name, context)


tupleView = Tuple.as_view()
