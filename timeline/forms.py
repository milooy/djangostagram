from django import forms

from .models import Post

class PostForm(forms.Form):
    image_url = forms.CharField(
        error_messages={
            'required': '이미지 주소를 입력해주세요.'
        },
        max_length=128, label="이미지 주소")
    text = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")
    tags = forms.CharField(
        required=False, label="태그")
