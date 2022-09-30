from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class UserRegistration(forms.Form):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

