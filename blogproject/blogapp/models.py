from pyexpat import model
from tkinter import CASCADE
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # 어떤 글에 대한 댓글인지 종속성 부여(foreign key) 및 글 삭제시 동시에 삭제
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    