from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Word
from .utils import DataMixin


letters_states = {
    "'": None, 'й': None, 'ц': None, 'у': None, 'к': None, 'е': None, 'н': None, 'г': None, 'ш': None, 'щ': None, 'з': None, 'х': None, 'ї': None,
    'ф': None, 'і': None, 'в': None, 'а': None, 'п': None, 'р': None, 'о': None, 'л': None, 'д': None, 'ж': None, 'є': None,
    '↵': None, 'я': None, 'ч': None, 'с': None, 'м': None, 'и': None, 'т': None, 'ь': None, 'б': None, 'ю': None, '←': None,
}

letters = [
    ["'", 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ї'],
    ['ф', 'і', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'є'],
    ['↵', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '←']
]

states = ['present', 'absent', 'correct', None]
index = 0


def some_func(request):
    global index
    if request.method == 'GET':
        param1 = request.GET.get('param_first')

        letters_states[param1] = states[index]
        index = index + 1 if index < 3 else 0

        context = {'response_data': param1,
                   'letters_states': letters_states}

        return JsonResponse(context)


def show_words(request):
    words = Word.objects.filter(word__iregex=r"^на")
    context = {'words': words,
               'letters': letters
               }
    return render(request, 'slovko/show_words.html', context=context)


class SlovkoBrut(DataMixin, ListView):
    model = Word
    template_name = 'slovko/brut.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Brut')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
