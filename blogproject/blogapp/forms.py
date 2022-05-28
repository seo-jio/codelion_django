#django form 생성
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta: #모델 적용
        model = Blog
        fields = '__all__' #모델 내 모든 속성을 다 받아옴
        #fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]