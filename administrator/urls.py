# urls.py
from administrator.views import test_template
from django.urls import path

urlpatterns = [
    path('test-template/', test_template, name='test-template'),
]
