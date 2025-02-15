import re
from django import forms
from .models import Contato
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'show', 'picture', 'category']

    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name.isalpha():
            raise ValidationError('Nome não pode conter valores numéricos!', code='invalid')
        
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        
        if not last_name.isalpha():
            raise ValidationError('Sobrenome não pode conter valores numéricos!', code='invalid')

        return last_name
# voltar neste trecho para corrigir a validação de telefone,
# permitir com que o usuário deixe () e - dentro do campo, 
# não deixar com que o usuário insira letras do alfabeto.

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name.isalpha():
            raise ValidationError('Nome não pode conter valores numéricos!', code='invalid')
        
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        
        if not last_name.isalpha():
            raise ValidationError('Sobrenome não pode conter valores numéricos!', code='invalid')

        return last_name

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Este email já esta cadastrado!'))
        
        return email
    

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required',
        error_messages={
            'min_lenght': 'Insira mais de 2 letras'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required',
        error_messages={
            'min_lenght': 'Insira mais de 2 letras'
        }
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Confirme a senha.',
        required=False,
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('As senhas não coincidem!'))
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error('password1', error)

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError('Nome não pode conter valores numéricos!', code='invalid')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError('Sobrenome não pode conter valores numéricos!', code='invalid')
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.email != email and User.objects.filter(email=email).exists():
            raise ValidationError('Este email já está cadastrado!')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user