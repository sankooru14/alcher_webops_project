
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>blog about</h1>')
@login_required
def myprofile(request):
    if request.user.is_authenticated:
        img = Image.objects.all()
        return render(request, 'blog/myprofile.html', {'img':img})
    else:
        return redirect('login')
def newpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            form.instance.author=request.user
            if form.is_valid():
                form.save()
                return redirect('blog-myprofile')
        form = ImageForm()
        return render(request, 'blog/newpost.html',{'form':form} )
    else:
        return render(request,'login')
def mypost(request):
    if request.user.is_authenticated:
        img = Image.objects.filter(author=request.user)
        return render(request, 'blog/mypost.html', {'img':img} )
    else:
        return render(request,'login')

def savedpost(request):
    if request.user.is_authenticated:
        
        return render(request, 'blog/savedpost.html',{'img':Image.objects.filter(favourites=request.user)})
    else:
        return redirect('login')

def favourite_add(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Image,id=id)
        if post.favourites.filter(id=request.user.id).exists():
            post.favourites.remove(request.user)
        else:
            post.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return redirect('login')

        
    