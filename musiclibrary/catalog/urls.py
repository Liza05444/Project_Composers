from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compositions/', views.CompositionListView.as_view(), name='compositions'),
    path('composition/<int:pk>', views.CompositionDetailView.as_view(), name='composition-detail'),
    path('composition/create/', views.CompositionCreate.as_view(), name='composition-create'),

    path('composers/', views.ComposerListView.as_view(), name='composers'),
    path('composer/<int:pk>', views.ComposerDetailView.as_view(), name='composer-detail'),
    path('composer/create/', views.ComposerCreate.as_view(), name='composer-create'),

    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genre/create/', views.GenreCreate.as_view(), name='genre-create'),
]
