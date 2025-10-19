# my_app/views.py
from django.shortcuts import render


def test_template(request):
    return render(request, 'drf_yasg/swagger-ui.html', {
        'title': 'L-SALES API Docs',
        'description': 'Test Description',
    })
