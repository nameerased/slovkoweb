from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', SlovkoHome.as_view(), name='homepage'),
    path('show_words/', show_words, name='show_words'),
    re_path(r'^brut/q', some_func),
    # path('brut/', SlovkoBrut.as_view(), name='brut'),
]
