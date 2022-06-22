from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    
    # 블로그 글들을 시간 오름차순으로 모조리 띄우는 코드
    #posts = Blog.objects.filter().order_by('date')

    # 블로그 글들을 시간 내림차순으로 모조리 띄우는 코드
    posts = Blog.objects.filter().order_by('-date')

    return render(request, 'index.html', {'posts':posts})    # 3번째 파라미터는 dict형

# 블로그 글 작성 html 을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()

    return redirect('home')


# django form 을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야 함
# POST 요청 (= 입력한 내용을 데이터베이스에 저장
# 둘다 받을 수 있음
def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})   # 3번째 파라미터는 dict형

# django modelform 을 이용해서 입력값을 받는 함수
def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()             # 모델을 기반으로 만든 모델폼은 폼자체가 save를 갖고 있음
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

# blog_id 를 파라미터로 전달해야함
def detail(request, blog_id):
    # blog_id 번째 블로그 글을 db에서 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드    

    comment_form = CommentForm()
    
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

# 댓글 기능 구현
def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
    return redirect('detail', blog_id)