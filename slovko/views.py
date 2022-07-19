from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import Word


letters_states = {
    "'": None, 'й': None, 'ц': None, 'у': None, 'к': None, 'е': None, 'н': None, 'г': None, 'ш': None, 'щ': None, 'з': None, 'х': None, 'ї': None,
    'ф': None, 'і': None, 'в': None, 'а': None, 'п': None, 'р': None, 'о': None, 'л': None, 'д': None, 'ж': None, 'є': None,
    '↵': None, 'я': None, 'ч': None, 'с': None, 'м': None, 'и': None, 'т': None, 'ь': None, 'б': None, 'ю': None, '←': None,
}

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
               }
    return render(request, 'slovko/show_words.html', context=context)
