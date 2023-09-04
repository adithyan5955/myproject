from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies 
    }
    return render(request, 'index.html', context)

def detail(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request,"detail.html",{'movie':movie}) 


def AddMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieapp:index') 
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})

def UpdateMovie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movieapp:detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'update.html', {'form': form, 'movie': movie})



def DeleteMovie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)    
    if request.method == 'POST':
        print(f"Deleting movie with ID {movie_id}")
        movie.delete()
        return redirect('movieapp:index')
    
    return render(request, 'detail.html', {'movie': movie})
