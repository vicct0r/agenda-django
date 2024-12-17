# Generated by Django 5.1.4 on 2024-12-15 22:18

import django.db.models.deletion
import stdimage.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_category_options_contato_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='pictures/%Y/%m/', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}}),
        ),
    ]