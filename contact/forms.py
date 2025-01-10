import re
from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'show', 'picture', 'category', 'owner']

    
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
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        phone = re.sub(r'\D', '', phone)  # Remove tudo que não for número

        # Verificar se o telefone contém apenas dígitos
        if not phone.isdigit():
            raise ValidationError('Este campo não pode conter letras!', code='invalid')

        return phone  # Retorna o valor original

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