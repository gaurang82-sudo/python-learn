from django.http import HttpResponse
from django.shortcuts import render
from .models import movie
# Create your views here.


def index(request):
    movies = movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def detail(request, movie_id):
    return HttpResponse(movie_id)
