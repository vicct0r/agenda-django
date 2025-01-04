from django import forms
from .models import Contato
from django.core.exceptions import ValidationError

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'show', 'picture', 'category', 'owner']

    
    # Validação personalizada do campo FIRST_NAME do meu formulário

    # def clean_first_name(self):
    #    first_name = self.cleaned_data.get('first_name')
    #
    #    if first_name == 'ABC':
    #        raise ValidationError('First_name não pode ser "ABC".')
    #    
    #    return first_name