from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    post_list=Post.objects.all()
    content = {
        'post_list':post_list
    }
    return render(request, 'board/index.html', content)

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    content = {
        'post':post
    }
    return render(request, 'board/posting.html', content)

def new_post(request):
    if request.method == 'POST':
        if request.POST['photo']:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                content = request.POST['content'],
                photo = request.POST['photo'],
            )
        else:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                content = request.POST['content'],
            )
        return redirect('/board/')
    return render(request, 'board/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/board/')
    return render(request, 'board/posting.html', {'Post': post})