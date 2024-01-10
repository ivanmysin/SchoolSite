from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

# Create your models here.

class SiteMenu(models.Model):
    pages_types = [ ("text", "Текст"), ("list_with_photo", "Список с фото"),]

    name = models.CharField('Отображение на сайте', max_length=50, blank=False)
    link = models.CharField('Ссылка (на английском)', max_length=50, blank=False)
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    page_type = models.CharField('Тип страницы', max_length=250, blank=False, choices=pages_types)
    is_show_top = models.BooleanField('Отображать на верхней панели?', blank=True, default=True)
    is_show_left = models.BooleanField('Отображать на левой панели?', blank=True, default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

class Organizators(models.Model):
    role = models.CharField('Роль в оргкоммитете', max_length=50, blank=True)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/orgs_photo/', blank=True, default="")
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', blank=True, default=True)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    # @property
    # def photo_preview(self):
    #     if self.path_to_photo:
    #         return mark_safe('<img src="{}" width="300" height="300" />'.format(self.path_to_photo.url))
    #     return ""
    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'



class Lectors(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    affilation = models.CharField('Место работы', max_length=200, blank=True)
    degree = models.CharField('Ученая степень/Ученое звание', max_length=50, blank=True)


    path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/lectors_photo/', blank=True, default="")
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'

class Partners(models.Model):
    organization_name = models.CharField('Название организации', max_length=250, blank=True)
    role = models.CharField('Роль в проведении школы', max_length=250, blank=True)
    organization_description = models.TextField('Описание организации', max_length=1000, blank=True)

    path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/partners_photo/', blank=True, default="")
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.organization_name)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

class KeyDates(models.Model):
    date_desription = models.CharField('Описание', max_length=150, blank=False)
    date = models.DateField('Ключевая дата', blank=False)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.date_desription)

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'

class Faqs(models.Model):
    question = models.CharField('Вопрос', max_length=250, blank=False)
    answer = RichTextField('Ответ', blank=False)
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Частые вопросы'

class TextPage(models.Model):
    pages = [
        ("lodging", "Размещение"),
        ("payment", "Оргвзнос"),
        ("contacts", "Контакты"),
        ("history", "История"),
    ]


    title = models.CharField('Заголовок', max_length=250, blank=False)
    text = RichTextField('Текст', blank=False)
    page = models.CharField('Страница, на которой будет отображаться', max_length=250, blank=False, choices=pages )
    path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/partners_photo/', blank=True, default="")
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Текст для страницы'
        verbose_name_plural = 'Тексты для страниц'

class QualifyingTasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок', max_length=250, blank=False)
    text = RichTextField('Текст задачи', blank=False)

    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Отборочная задача'
        verbose_name_plural = 'Отборочные задачи'


class ApplicationsForParticipation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя', max_length=250, blank=False)
    surname = models.CharField('Фамилия', max_length=250, blank=False)
    patronymic = models.CharField('Отчество', max_length=250, blank=False)
    email = models.EmailField('Почта', max_length=250, blank=False)
    phone = models.CharField('Телефон', max_length=20, blank=False)
    university = models.CharField('ВУЗ', max_length=12, blank=False)
    education_stage = models.CharField('Стадия обучения', max_length=250, blank=False)
    form_of_participation = models.CharField('Форма участия', max_length=250, blank=False)

    expirience = models.TextField('Опыт в нейронауке', max_length=5000, blank=False)
    about_participant = models.TextField('Расскажите о себе', max_length=5000, blank=False)
    qualifying_answers = models.TextField('Ответы на отборочные задачи', max_length=50000, blank=True)


    sended_datetime = models.DateTimeField('Время отправки формы', blank=False, auto_now=True)

    is_accepted = models.BooleanField('Берем на школу?', default=False)

    #order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)



    def __str__(self):
        return "{}".format(self.surname)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class QualifyingAnswers(models.Model):
    participant_id = models.ForeignKey(ApplicationsForParticipation, on_delete=models.CASCADE, blank=False)
    task_id = models.ForeignKey(QualifyingTasks, on_delete=models.CASCADE, blank=False)
    answer = models.TextField('Ответ на отборочную задачу', max_length=50000, blank=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'