from django.urls import path
from .views import *
app_name = 'Questions'

urlpatterns = [
    path('', new_question, name='new_question'),
    path('responses', question_list, name='question_list'),
    path('success', success, name='success'),
]