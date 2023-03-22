from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'Year': 1979
        }, 
        {
            'id': 6,
            'title': 'Sharknado',
            'Year': 2015
        },
        {
            'id': 7,
            'title': 'The Meg',
            'Year': 2020
        }
        ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")