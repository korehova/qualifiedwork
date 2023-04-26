import os

from django.contrib.auth import logout, authenticate, login
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from qualifiedwork import settings
from .models import Category, File
from .forms import *


# Create your views here.


def index(request):
    return render(request, 'mycloud/index.html')


def about(request):
    return render(request, 'mycloud/about.html')


def workspace(request):
    category = request.GET.get('category')
    categories = Category.objects.all()
    if category == None:
        files = File.objects.filter(users=request.user.id)
    else:
        files = File.objects.filter(users=request.user.id, category__name=category)
    files = files.order_by('-date')
    context = {'categories': categories, 'files': files}
    return render(request, 'mycloud/workspace1.html', context=context)


def share(request, pk, username):
    user = User.objects.get(username=username)
    if user:
        file = File.objects.get(id=pk)
        print(file)
    else:
        print('user not found')


def addFile(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        file = request.FILES.get('file')
        if 'image' in file.content_type:
            ftype = 'Изображения'
        else:
            ftype = 'Текстовые файлы'
        ftype=Category.objects.get(name=ftype)
        obj = File.objects.create(
            category=ftype,
            file=file,
        )
        obj.users.add(request.user)
        return redirect('workspace')
    return render(request, 'mycloud/add.html', context={'categories': categories})


def remove_file(request, pk):
    file = File.objects.filter(id=pk)[0]
    os.remove(file.file.path)
    file.delete()
    categories = Category.objects.all()
    files = File.objects.filter(users=request.user.id)
    context = {'categories': categories, 'files': files}
    return render(request, 'mycloud/workspace1.html', context=context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type='application/adminupload')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


def viewFile(request, pk):
    files = File.objects.get(id=pk)
    return render(request, 'mycloud/view.html', context={'files': files})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # flash
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'mycloud/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username):
            return HttpResponse("Имя занято")
        if password1 != password2:
            # flash + проверка на наличие ника в бд
            return HttpResponse("Your password and conform password are not Same!!")
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('home')
    return render(request, 'mycloud/index.html')


def logout_user(request):
    logout(request)
    return redirect('home')
