from django.views.generic import TemplateView


class Index(TemplateView):
    # テンプレートファイル連携
    template_name = 'practice/sets/index.html'

    print('*' * 5 + '練習28' + '*' * 5)
    a = {1, 2, 3, 4, 5, 6}
    b = {2, 3, 6, 7}

    print(a - b)
    print(b - a)

    # aにもありbにもあるもの
    print(a & b)

    # aとbに含まれるもの（重複は除く）
    print(a | b)

    # aにもありbにもあるもの以外
    print(a ^ b)

    print('*' * 5 + '練習29' + '*' * 5)

    # 集合の値の追加
    s = {1, 2, 3, 4, 5}
    s.add(6)
    print(s)

    # 集合の値の削除
    s.remove(6)
    print(s)

    s.clear()
    print(s)

    my_friends = {'A', 'C', 'D'}
    A_friend = {'B', 'D', 'E', 'F'}
    print(my_friends & A_friend)