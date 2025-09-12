from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_vote', views.submit_vote, name='submit_vote'),
]