from django.views.generic import TemplateView


class Index(TemplateView):
    # count = 0
    # while count < 5:
    #     print(count)
    #     count += 1
    # else:
    #     print('count done')
    #
    # count_2 = 0
    # while True:
    #     if count_2 >= 5:
    #         break
    #     if count_2 == 2:
    #         count_2 += 1
    #         continue
    #     print(count_2)
    #     count_2 += 1
    #
    # i = 0
    #
    # some_list = [1, 2, 3, 4, 5]
    # while i < len(some_list):
    #     print(some_list[i])
    #     i += 1
    #
    # for i in some_list:
    #     print(i)

    for s in 'abcde':
        print(s)

    for word in ['My', 'name', 'is', 'mike']:
        print(word)

    for word in ['My', 'name', 'is', 'mike']:
        if word == 'name':
            break
        print(word)

    for word in ['My', 'name', 'is', 'mike']:
        if word == 'name':
            continue
        print(word)

    for fruit in ['apple', 'banana', 'orange']:
        if fruit == 'banana':
            print('stop eating')
            break
        print(fruit)
    else:
        print('I ate all!')

    for i in range(10):
        print(i)

    for i in range(2, 10):
        print(i)

    for i in range(2, 10, 3):
        print(i)

    for i in range(10):
        print(str(i) + ':hello!')

    for _ in range(10):
        print('hello!')

    for i, fruit in enumerate(['apple', 'banana', 'orange']):
        print(i, fruit)

    days = ['Mon', 'Tue', 'Wed']
    fruit = ['apple', 'banana', 'orange']
    drinks = ['coffee', 'tea', 'beer']

    for day, fruit, drinks in zip(days, fruit, drinks):
        print(day, fruit, drinks)

    d = {'x': 100, 'y': 200}

    for key, value in d.items():
        print(key, ':', value)

    # テンプレートファイル連携
    template_name = 'practice/while_practice/index.html'


whilePracticeView = Index.as_view()
