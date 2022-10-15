from django.shortcuts import render


def index(request):
    print(what_is_this('red'))
    print(what_is_this('green'))
    print(what_is_this('yellow'))

    get_menu(entree='chicken', drink='beer')

    x = [1, 2, 3]
    r = append_list(100, x)
    print(r)

    x = [1, 2, 3]
    r = append_list(200, x)
    print(r)

    say_something('Hi!', 'Mike', 'Nancy')

    t = ('Mike', 'Nancy')
    say_something('Hi!', *t)

    d = {
        'entree': 'beef',
        'drink': 'ice coffee',
        'dessert': 'ice',
    }
    get_dict_menu(**d)

    get_args_manu('banana', 'apple', 'orange', entree='beef', drink='wine', dessert='ice')

    outer(1, 2)

    f = outer2(1, 2)
    r = f()
    print(r)

    ca1 = circle_area_func(3.14)
    ca2 = circle_area_func(3.141592)
    print(ca1(10))
    print(ca2(10))

    # デコレータメソッド
    @print_info
    def add_num(a, b):
        return a + b

    r = add_num(10, 20)
    print(r)

    # デコレータメソッド
    @print_info
    @print_more
    def subtraction(a, b):
        return a - b

    r = subtraction(30, 12)
    print(r)

    # ラムダ
    lambda_sample_func()

    # ジェネレーター
    greet_generate()

    # リスト内包表記
    list_test_func()

    # 辞書包括表記
    dic_test_func()

    # 集合包括表記
    set_test_func()

    # 例外処理
    exception_test()

    return render(request, 'practice/func/index.html')


def what_is_this(color):
    """
    色を入力すると野菜を出力する
    :param color: red, green
    :return: red: tomato, green: green pepper,
             other: I don't know
    """
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


def get_menu(entree='beef', drink='wine', dessert='ice'):
    """
    メニューを出力する
    :param entree: メイン
    :param drink: ドリンク
    :param dessert: デザート
    """
    print(entree)
    print(drink)
    print(dessert)


def append_list(x, list_item=None):
    """
    配列に値を追加する
    :param x: 追加する値
    :param list_item: 追加元の配列
    :return: xが追加されたリスト
    """
    if list_item is None:
        list_item = []
    list_item.append(x)
    return list_item


def say_something(word, *args):
    """
    wordとタプル化された引数の値を出力する
    :param word:
    :param args:
    :return:
    """
    print(word)
    for arg in args:
        print(arg)


def get_dict_menu(**kwargs):
    """
    引数のdict型の値を展開して出力する
    :param kwargs:
    :return:
    """
    for k, v in kwargs.items():
        print(k, v)


def get_args_manu(food, *args, **kwargs):
    """
    引数の文字列とタプル型、dict型を展開する
    :param food:
    :param args:
    :param kwargs:
    :return:
    """
    print(food)
    print(args)
    print(kwargs)


def outer(a, b):
    """
    外部関数の使い方テスト
    a + b + a + bを実行します
    :param a: 追加したい値1
    :param b: 追加したい値2
    :return:
    """

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)


def outer2(a, b):
    """
    クロージャー関数の使い方のテスト
    :param a: 数字
    :param b: 数字
    :return: a + b の関数を返す
    """

    def inner():
        return a + b

    return inner


def circle_area_func(pi):
    """
    円の面積の計算用のクロージャ
    :param pi:
    :return:circle_area
    """

    def circle_area(radius):
        return pi * radius * radius

    return circle_area


def print_info(func):
    """
    処理の開始に「start」、終わりに「end」を出力するデコレータメソッド
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


def print_more(func):
    """
    関数の処理の最初に引数を確認し、終わりに結果を返す
    デコレータメソッド
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        print('func: ', func.__name__)
        print('args: ', args)
        print('kwargs: ', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


def lambda_sample_func():
    """
    ラムダの練習メソッド
    :return:
    """
    list_item = ['Mon', 'tue', 'Wed', 'Wed', 'Tue', 'fri', 'sat', 'sun']

    def change_word(words, func):
        for word in words:
            print(func(word))

    def capitalize_word(word):
        return word.capitalize()

    def lower_word(word):
        return word.lower()

    change_word(list_item, capitalize_word)
    change_word(list_item, lower_word)

    # 配列の値を大文字に変換する
    change_word(list_item, lambda word: word.capitalize())
    # 配列を小文字にする
    change_word(list_item, lambda word: word.lower())


def greet_generate():
    greeting_list = ['Good morning', 'Good afternoon', 'Good night']
    for i in greeting_list:
        print(i)

    def counter(num=10):
        for _ in range(num):
            yield 'run'

    def greeting():
        yield 'Good morning'
        yield 'Good afternoon'
        yield 'Good night'

    g = greeting()
    c = counter()

    print(next(g))
    print(next(c))
    print("@@@@@@")
    print(next(g))
    print(next(c))
    print("@@@@@@")
    print(next(g))
    print(next(c))


def list_test_func():
    """
    リスト内包表記
    :return:
    """
    t = [1, 2, 3, 4, 5]
    t2 = [5, 6, 7, 8, 9, 10]

    r = []
    for i in t:
        if i % 2 == 0:
            r.append(i)

    print(r)

    r = [i for i in t if i % 2 == 0]
    print(r)

    r = []
    for i in t:
        for j in t2:
            r.append(i * j)
    print(r)

    r = [i * j for i in t for j in t2]
    print(r)


def dic_test_func():
    """
    辞書内包表記
    :return:
    """
    w = ['mon', 'tue', 'wed']
    f = ['coffee', 'milk', 'water']

    d = {}
    for x, y in zip(w, f):
        d[x] = y

    print(d)

    d = {x: y for x, y in zip(w, f)}
    print(d)


def set_test_func():
    """
    集合内包表記
    :return:
    """
    s = set()
    for i in range(10):
        if i % 2 == 0:
            s.add(i)

    s = {i for i in range(10) if i % 2 == 0}
    print(s)


def generator_test_func():
    def g():
        for i in range(10):
            yield i

    g = g()
    print(type(g))

    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    # ジェネレーター内包表記
    g = (i for i in range(10))

    print(type(g))

    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    g = tuple(i for i in range(10))
    print(type(g))

    print(g)


def exception_test():
    list_item = [1, 2, 3]
    try:
        list_item[5]
    except IndexError as ex:
        print("Don't worry: {}".format(ex))

    except NameError as ex:
        print(ex)

    except Exception as ex:
        print('other:{}'.format(ex))
    else:
        print('done')
    finally:
        print('clean up')


class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
    try:
        check()
    except UppercaseError as exc:
        print('This is may fault. Go next')
