from django import forms
from courses.models import Course
# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)


# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    username = forms.CharField(max_length=254, label="Имя пользователя")
    first_name = forms.CharField(max_length=254, label="Имя")
    last_name = forms.CharField(max_length=254, label="Фамилия")
    email = forms.EmailField(max_length=254, label="Адрес электронной почты")
    password1 = forms.CharField(max_length=254, label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=254, label="Повторите пароль", widget=forms.PasswordInput())


    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2',)