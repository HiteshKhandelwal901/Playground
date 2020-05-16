from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import test_Form
from django.contrib import messages
from django.shortcuts import  get_object_or_404
  

from .models import Post


# Create your views here.

#def Postlist(request):
    #posts = Post.objects.order_by('-publish')
    #context = {'title': "Hello world ", 'cal': "So far so good !", "post" : posts}
 #   return render(request, 'index.html', context)

def get_name(request):

    posts = Post.objects.order_by('-publish')
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = test_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Your password was updated successfully!') 
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = test_Form()
    context = {'title': "Hello world ", 'cal': "So far so good !", "post" : posts, "form": form}
    return render(request, 'index.html',context)

def detail_post(request, slug):
    D_post =  get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', context = {'title': "Hello world ", 'cal': "So far so good !", "post" : D_post} )   