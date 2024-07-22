from django.forms import *


class UserRegister(Form):
    username = CharField(max_length=30, label='Введите Ваше имя:', initial='alpha')
    password = CharField(widget=PasswordInput(), min_length=8, label='Введите пароль:')
    repeat_password = CharField(widget=PasswordInput(), min_length=8, label='Повторите пароль:')
    age = IntegerField(max_value=150, label='Возраст:')  # min_value=18

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('repeat_password')
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError('Пароли не совпадают!')
    #     return password2
