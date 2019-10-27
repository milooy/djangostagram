from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={'required' : '아이디를 입력하세요'},
        max_length=32,
        label="사용자 이름")
    password = forms.CharField(
        error_messages={'required' : '비밀번호를 입력하세요'},
        widget=forms.PasswordInput,
        label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        print(username, password)

        if username and password:
            try:
                dsuser = Dsuser.objects.get(username=username)
            except Dsuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다')
                return

            if not check_password(password, dsuser.password):
                self.add_error('username', '비밀번호를 틀렸습니다')
            else:
                self.user_id = dsuser.id

    class Meta:
        model = Dsuser
        fields = ('username', 'password')