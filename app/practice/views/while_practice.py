from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):

    def __main__(self):
        self.main()

    @staticmethod
    def main():
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

    def get(self, request, *args, **kwargs):
        self.main()
        return render(request, 'practice/while_practice/index.html')


whilePracticeView = Index.as_view()
