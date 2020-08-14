from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    #output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)   #first arg is model class Movie
    return render(request, 'movies/detail.html', {'movie': movie})
    # try:
    #    movie = Movie.objects.get(pk=movie_id)
    #    return render(request, 'movies/detail.html', {'movie': movie})
    #    # return HttpResponse(movie_id)
    # except Movie.DoesNotExist:
    #    raise Http404()
