# urls.py
from administrator.views import test_template
from django.urls import path

urlpatterns = [
    path('docs/', test_template, name='test-template'),
]
