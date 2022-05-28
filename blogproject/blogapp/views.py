from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {"posts":posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()  #현제 시간 저장
        post.save() #데이터베이스에 객체 저장
    return redirect('home') #다른 logic으로 이동

def formcreate(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():  #form내 값들이 유효한지 판단
            post = Blog()
            post.title = form.cleaned_data['title']  #cleaned_data : 검증된 데이터
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        print("===========================6^^^")
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == "POST" or "FILES":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  #model form 내에 save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form}) #html 파일에 form을 넘겨 주기 위해서는 딕셔너리 형태를 사용

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)

def logout(request):
    auth.logout(request)
    return redirect('home')