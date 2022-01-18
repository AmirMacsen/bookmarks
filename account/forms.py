from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密码",
                               widget=forms.PasswordInput)

    password2 = forms.CharField(label="再次输入密码",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("密码不一致")

            return cd['password2']


class UserEditForm(forms.ModelForm):
    username = forms.CharField(validators=[MinLengthValidator(3, message="用户名最小长度为3"),
                                           MaxLengthValidator(20, message="用户名最大长度为20")],
                               label="用户名")

    class Meta:
        model = User
        fields = ("email",)

    field_order = ['username',"email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]
