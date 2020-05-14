from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.

def Postlist(request):
    posts = Post.objects.order_by('-publish')
    context = {'title': "Hello world ", 'cal': "So far so good !", "post" : posts}
    return render(request, 'index.html', context)