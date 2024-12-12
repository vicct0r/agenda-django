from django.db import models
from stdimage import StdImageField
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('categoria', max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Contato(models.Model):
    first_name = models.CharField('nome', max_length=100)
    last_name = models.CharField('sobrenome', max_length=100)
    phone = models.CharField('telefone', max_length=12)
    email = models.EmailField('email', max_length=90)
    created_date = models.DateTimeField(default=timezone.now) # não execute timezone, o django que será responsável por executa-lo
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = StdImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, verbose_name='owner', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'