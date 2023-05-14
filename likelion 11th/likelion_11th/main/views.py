from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts' : posts})
def setting(request):
    return render(request, 'main/setting.html')
def study(request):
    return render(request, 'main/study.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.week = request.POST['week']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.feel = request.POST['feel']
    new_post.author = request.user
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post':post})

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.week = request.POST['week']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.feel = request.POST['feel']
    if request.FILES.get('image') != None:
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:mainpage')