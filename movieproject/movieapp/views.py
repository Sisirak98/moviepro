from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import movie
from .forms import movieforms


def home(request):
    m = movie.objects.all()
    c = {
        'mlist': m
    }
    return render(request, "index.html", c)


def detail(request,mid):
    mv=movie.objects.get(id=mid)
    return render(request,"detail.html",{'m':mv})


def add(request):
    if request.method =='POST':
        name = request.POST.get('name',)
        des = request.POST.get('des',)
        year = request.POST.get('year',)
        im = request.FILES['im']
        m=movie(name=name,des=des,year=year,im=im)
        m.save()

    return render(request,'add.html')
def update(request,id):
    m= movie.objects.get(id=id)
    form = movieforms(request.POST or None, request.FILES,instance=m)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'m':m})


def delete(request, id):
    if request.method == 'POST':
        m = movie.objects.get(id=id)
        m.delete()
        return redirect('/')
    return render(request,'delete.html')