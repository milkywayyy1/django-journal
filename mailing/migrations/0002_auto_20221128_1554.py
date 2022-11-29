# Generated by Django 3.0.8 on 2022-11-28 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing_from', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='to_users',
            field=models.ManyToManyField(related_name='mailing_to', to=settings.AUTH_USER_MODEL, verbose_name='Получатели'),
        ),
    ]
