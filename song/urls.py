from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchSong().as_view())
]
