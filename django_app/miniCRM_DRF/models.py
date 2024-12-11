from django.contrib.auth.models import User
from django.db import models


class Funnel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Название', max_length=50)
    user = models.ForeignKey(User, verbose_name='Пользоватлеь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Stage(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Название', max_length=50)
    user = models.ForeignKey(User, verbose_name='Пользоватлеь', on_delete=models.CASCADE)
    funnel = models.ForeignKey(
        Funnel,
        on_delete=models.CASCADE,
        related_name='stage',
        verbose_name='Воронка',
        null=True
    )

    def __str__(self):
        return self.name

class Deal(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=256, null=True)
    user = models.ForeignKey(User, verbose_name='Пользоватлеь', on_delete=models.CASCADE)
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='deal',
        verbose_name='Этап',
        default= 1
    )

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    email = models.CharField('E-mail', max_length=250)
    adress = models.CharField('Адрес', max_length=250)
    user = models.ForeignKey(User, verbose_name='Пользоватлеь', on_delete=models.CASCADE)
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name='Сделка',
        null=True
    )