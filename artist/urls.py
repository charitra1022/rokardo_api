from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.GetTopArtists().as_view()),
]
