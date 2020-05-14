from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Postlist, name='main-view'),
    
]