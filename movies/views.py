from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


class MoviesViews(View):
    """list of movies"""

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    """Full description of movie"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, "movies/movie_detail.html", {"movie": movie})

