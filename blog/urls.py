from django.urls import include, path

from . import views

urlpatterns = [
    #path('', views.Postlist, name='main-view'),
    path('', views.get_name, name='main-form-view'),
    path('<slug:slug>', views.detail_post, name='detail-post')
    
]