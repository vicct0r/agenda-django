# Generated by Django 5.1.4 on 2024-12-11 13:13

import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='categoria')),
            ],
        ),
        migrations.AddField(
            model_name='contato',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='pictures/%Y/%m/', variations={}),
        ),
        migrations.AddField(
            model_name='contato',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.category', verbose_name='contact_category'),
        ),
    ]
