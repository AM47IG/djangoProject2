from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game
from .serializers import GameSerializer


# Create your views here.
class GameAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def games(request):
    list_games = Game.objects.all()
    context = {'games': list_games}
    return render(request, 'fourth_task/games.html', context)


def sign_up_by_django(request):
    users = map(lambda query: query.name, list(Buyer.objects.all()))
    form = UserRegister()
    info = {'form': form}
    if request.method == 'POST':
        form = UserRegister(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            username = username if username not in users else None
            password = form.cleaned_data.get('password') == form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')
            age = age if age >= 18 else None
            if username and password and age:
                Buyer.objects.create(name=username, age=age)
                return render(request, 'fourth_task/menu.html', context=info)
            if not username:
                info['error'] = 'Пользователь уже существует'
            elif not password:
                info['error'] = 'Пароли не совпадают'
            elif not age:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'fifth_task/registration_page.html', context=info)
