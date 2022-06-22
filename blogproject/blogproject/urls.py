from socket import create_connection
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form 을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form 을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform 을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 127.0.0.1:8000/detail/글번호
    path('detail/<int:blog_id>', views.detail, name='detail'),

    # 댓글 저장
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    # 로그인 기능
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
]
