from django.http import HttpResponse


class index():
    template_name = 'practice/index.html'

    def get_context_data(self, **kwargs):
        num = 1
        name = 'Mike'
        context = super().get_context_data(**kwargs)
        context["num"] = num
        context["name"] = name
        return context