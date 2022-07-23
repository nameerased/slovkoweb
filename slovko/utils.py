from django.db.models import Count
from .models import *

menu = [{'title': "Brut", 'url_name': 'brut'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        ]

letters = [
    ["'", 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ї'],
    ['ф', 'і', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'є'],
    ['↵', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '←']
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        # context['cats'] = cats
        context['letters'] = letters
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
