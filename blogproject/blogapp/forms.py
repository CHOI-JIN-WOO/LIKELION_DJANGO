from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__'             # 전체
        fields = ['title', 'body']      # 특정 필드만


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'             # 전체
        fields = ['comment']            # 특정 필드만

