from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
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
    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.week = request.POST['week']
        new_post.pub_date = timezone.now()
        words = request.POST['body'].split('#')
        new_post.body = words[0]
        new_post.feel = request.POST['feel']
        new_post.author = request.user
        new_post.image = request.FILES.get('image')
        new_post.save()
        tag_list = []
        tag_count = 0;
        for w in words:
            if (tag_count > 0 and len(w) > 0):
                tag_same = 0;
                w = w.split()[0]
                for t in tag_list:
                    if t == w:
                        tag_same = 1
                if tag_same == 0:
                    tag_list.append(w)
            tag_count += 1
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)
        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments':comments,})
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.author = request.user
        words = request.POST['content'].split('#')
        new_comment.content = words[0]
        new_comment.pub_date = timezone.now()
        new_comment.save()
        tag_list = []
        tag_count = 0;
        for w in words:
            if (tag_count > 0 and len(w) > 0):
                tag_same = 0;
                w = w.split()[0]
                for t in tag_list:
                    if t == w:
                        tag_same = 1
                if tag_same == 0:
                    tag_list.append(w)
            tag_count += 1
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_comment.tags.add(tag.id)
        return redirect('main:detail', id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user == update_post.author:
            update_post.title = request.POST['title']
            update_post.author = request.user
            update_post.week = request.POST['week']
            update_post.pub_date = timezone.now()
            words = request.POST['body'].split('#')
            update_post.body = words[0]
            update_post.feel = request.POST['feel']
            if request.FILES.get('image') != None:
                update_post.image = request.FILES.get('image')
            update_post.save()
            update_post.tags.clear()
            tag_list = []
            tag_count = 0;
            for w in words:
                if (tag_count > 0 and len(w) > 0):
                    tag_same = 0;
                    w = w.split()[0]
                    for t in tag_list:
                        if t == w:
                            tag_same = 1
                    if tag_same == 0:
                        tag_list.append(w)
                tag_count += 1
            for t in tag_list:
                
                tag, boolean = Tag.objects.get_or_create(name=t)
                update_post.tags.add(tag.id)
            return redirect('main:detail', update_post.id)
    return redirect('accounts/login')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:mainpage')

def delete_com(request, id):
    delete_comment = Comment.objects.get(id=id)
    post = delete_comment.post
    delete_comment.delete()
    return redirect('main:detail', post.id)

def tag_list(request):
    tags = Tag.objects.all()

    return render(request, 'main/tag_list.html', {'tags':tags,})

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    comments = tag.comments.all()
    return render(request, 'main/tag_posts.html', {'tag':tag, 'posts':posts, 'comments':comments,})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']      
        tag = get_object_or_404(Tag, name=searched)
        posts = tag.posts.all()
        comments = tag.comments.all()
        return render(request, 'main/search.html', {'tag': tag, 'posts':posts, 'comments':comments})
    else:
        return render(request, 'main/tag_list.html')