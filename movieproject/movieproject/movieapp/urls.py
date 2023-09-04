from django.urls import path
from . import views
app_name = 'movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.AddMovie, name='addmovie'),
    path('update/<int:movie_id>/', views.UpdateMovie, name='updatemovie'),
    path('delete/<int:movie_id>/', views.DeleteMovie, name='deletemovie'),

]
