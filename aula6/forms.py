from django import forms


class ContatoForm(forms.Form):
    first_name = forms.CharField(label='Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='Email')
    twitter = forms.URLField(label='Twitter')
