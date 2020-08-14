from django.urls import path
from . import views

app_name = 'movies' #django knows this variable makes code clean

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
    #path('', views.index, name='movies_index'),
    #path('<int:movie_id>', views.detail, name='movies_detail')
]
