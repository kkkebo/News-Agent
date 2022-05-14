import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import News

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail адрес', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title