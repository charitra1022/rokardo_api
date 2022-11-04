from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.GetTopArtists().as_view()),
    path('page/', views.GetArtistByMbid().as_view()),

]
