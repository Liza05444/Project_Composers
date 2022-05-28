from django.shortcuts import render

from .models import GenreModel, ComposerModel, CompositionModel
from django.views import generic
from django.views.generic.edit import CreateView


def index(request):
    num_compositions = CompositionModel.objects.all().count()
    num_composers = ComposerModel.objects.all().count()
    num_genres = GenreModel.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={'num_composers': num_composers, 'num_compositions': num_compositions, 'num_genres': num_genres})


class CompositionListView(generic.ListView):
    model = CompositionModel


class CompositionDetailView(generic.DetailView):
    model = CompositionModel


class CompositionCreate(CreateView):
    model = CompositionModel
    fields = ['composer', 'title', 'description', 'first_night', 'genre', 'audio', 'description_of_audio']


class ComposerListView(generic.ListView):
    model = ComposerModel


class ComposerDetailView(generic.DetailView):
    model = ComposerModel


class ComposerCreate(CreateView):
    model = ComposerModel
    fields = ['fio', 'biography', 'date_of_birth', 'date_of_death', 'photo']


class GenreListView(generic.ListView):
    model = GenreModel


class GenreDetailView(generic.DetailView):
    model = GenreModel


class GenreCreate(CreateView):
    model = GenreModel
    fields = ['name', 'definition', 'history']