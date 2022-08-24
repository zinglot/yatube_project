from django.shortcuts import render


from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('функция groups')


def groups_pk(request, pk):
    return HttpResponse(f'groups {pk}')