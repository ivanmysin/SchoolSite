from django.db import models

# Create your models here.
class Organizators(models.Model):
    role = models.CharField('Роль в оргкоммитете', max_length=50, blank=True)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    path_to_photo = models.CharField('Путь к фото', max_length=50, blank=True, default="")
    order = models.IntegerField('order', default=100)
    is_show = models.BooleanField('is_show', blank=True, default=True)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Оганизатор'
        verbose_name_plural = 'Оганизаторы'


class Lectors(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    affilation = models.CharField('Место работы', max_length=200, blank=True)
    degree = models.CharField('Ученая степень/Ученое звание', max_length=50, blank=True)


    path_to_photo = models.CharField('Путь к фото', max_length=50, blank=True, default="")
    order = models.IntegerField('order', default=100)
    is_show = models.BooleanField('is_show', default=True)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'

class Partners(models.Model):
    organization_name = models.CharField('Название организации', max_length=250, blank=True)
    role = models.CharField('Роль в проведении школы', max_length=250, blank=True)
    organization_description = models.TextField('Описание организации', max_length=1000, blank=True)

    path_to_photo = models.CharField('Путь к фото', max_length=50, blank=True, default="")
    order = models.IntegerField('order', default=100)
    is_show = models.BooleanField('is_show', default=True)


    def __str__(self):
        return "{}".format(self.organization_name)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

class KeyDates(models.Model):
    date_desription = models.CharField('Описание', max_length=150, blank=False)
    date = models.DateField('Ключевая дата', blank=False)
    is_show = models.BooleanField('is_show', default=True)


    def __str__(self):
        return "{}".format(self.date_desription)

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'