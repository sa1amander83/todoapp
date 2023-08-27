from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from todo.models import TodoModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'id': 'id_username', 'autocomplete': 'username'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
                                                                 'autocomplete': 'current-password'}))
    # remember = forms.BooleanField(label="Запомнить меня", widget=forms.CheckboxInput(
    #     attrs={'class': 'form-control form-control-user', 'id': 'remember'}
    # ))





class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'id': 'id_username', 'autocomplete': 'username',
               'autofocus': 'on'}))

    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
                                                                  'autocomplete': 'current-password'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
                                                                  'autocomplete': 'current-password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class DateStart(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'

class TimeStart(forms.TimeInput):
    input_type = 'time'
    format = '%H:%i'


class AddTodoForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ['todo_short_description', 'todo_full_description','todo_start_date', 'todo_start_time']

        widgets = {
            'todo_short_description': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'todo_full_description': forms.Textarea(attrs={'class': 'form-control form-control-user', 'col':3}),
            'todo_start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control form-control-user',
                       'type': 'date'
                       }),
            'todo_start_time': TimeStart(attrs={'class': 'form-control form-control-user'}),
            # 'todo_status': forms.CheckboxInput(attrs={'class': 'form-control form-control-user'}),
        }
