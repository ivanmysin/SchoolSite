from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField


class SiteMenu(models.Model):
    pages_types = [
        ("text", "Текст"),
        ("list_with_photo", "Список с фото"),
        ("list_with_accordion", "Список с раскрывающимися элементами"),
        ("form", "Форма заявки"),
        ("dates", "Даты"),
        ("contacts", "Контакты"),
    ]

    id = models.AutoField(primary_key=True)

    name = models.CharField('Отображение на сайте', max_length=50, blank=False)
    link = models.CharField('Ссылка (на английском)', max_length=50, blank=True, unique=True)
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    page_type = models.CharField('Тип страницы', max_length=250, blank=False, choices=pages_types, default="text")
    is_show_top = models.BooleanField('Отображать на верхней панели?', blank=True, default=True)
    is_show_left = models.BooleanField('Отображать на левой панели?', blank=True, default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class CommonSettings(models.Model):
    types = [
        ("big_title_text", "Большой текст в шапке сайта"),
        ("little_titlt_text", "Маленькая подпись в шапке сайта"),
        ("accept_applications", "Принимаем заявки?"),
    ]

    setting_name = models.CharField('Тип настройки', max_length=150, blank=False, unique=True, choices=types)
    setting_value = models.CharField('Значение', max_length=150, blank=True)
    def __str__(self):
        return self.setting_name

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Общие настройки сайта'


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

class FormatsOfParticipation(models.Model):

    format_participation = models.CharField('Форма участия', max_length=50, blank=False)
    is_show = models.BooleanField('Отображать на сайте?', default=True)
    def __str__(self):
        return "{}".format(self.format_participation)

    class Meta:
        verbose_name = 'Форма участия'
        verbose_name_plural = 'Формы участия'

class ApplicationsForParticipation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя', max_length=250, blank=False)
    surname = models.CharField('Фамилия', max_length=250, blank=False)
    patronymic = models.CharField('Отчество', max_length=250, blank=False)
    email = models.EmailField('Почта', max_length=250, blank=False)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    university = models.CharField('ВУЗ', max_length=150, blank=True)
    faculty = models.CharField('Факультет', max_length=150, blank=True)

    education_stage = models.CharField('Стадия обучения', max_length=150, blank=False)
    form_of_participation = models.CharField('Форма участия', max_length=150, blank=False)

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

class Contacts(models.Model):
    types = [
        ("phone", "Телефон"),
        ("email", "Почта"),
        ("link", "Ссылка"),
        ("another", "Другое"),
    ]
    site_subscript = models.CharField('Подпись на сайте', max_length=50, blank=True, default="")
    contact = models.CharField('Контактные данные', max_length=250, blank=False)
    contact_type = models.CharField('Тип контакта', max_length=50, blank=False, choices=types)


    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)


    def __str__(self):
        return "{}".format(self.site_subscript)
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Наши контакты'

class Gallery(models.Model):

    path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/gallery/', blank=True, default="")
    url = models.URLField('URL на внешний ресурс', blank=True, default="", max_length=250)
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', blank=True, default=True)
    is_show_in_header = models.BooleanField('Отображать в загловке сайта?', blank=True, default=False)
    is_show_in_common_gallery = models.BooleanField('Отображать в общей галерее?', blank=True, default=True)
    comment = models.CharField('Комментарий (не отображается на сайте)', blank=True, max_length=250)

    def __str__(self):
        return "{} {}".format(self.id, self.comment)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

# class GalleryTextConnections(models.Model):
#
#     text = models.ForeignKey(TextPage, on_delete=models.DO_NOTHING, related_name="article")
#     photo = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING, related_name="gallery")
#
#     def __str__(self):
#         return "{} {}".format(self.text_id.title, self.photo_id.comment)
#
#     class Meta:
#         verbose_name = 'Связь'
#         verbose_name_plural = 'Связи текстов и картинок'

class TextPage(models.Model):
    # class PagesChoise(Choices):
    #     choices = []
    #     def __init__(self):
    #         pages = SiteMenu.objects.filter(page_type='text').values()
    #
    #
    #         for p in pages:
    #             PagesChoise.choices.append((p.link, p.name))


    id = models.AutoField(primary_key=True)

    title = models.CharField('Заголовок', max_length=250, blank=False)
    text = RichTextField('Текст', blank=False)

    #page = models.CharField('Страница, на которой будет отображаться', max_length=250, blank=False, choices=pages )
    page = models.ForeignKey(SiteMenu, on_delete=models.CASCADE)

    # path_to_photo = models.ImageField('Фото', upload_to='./static/main/images/partners_photo/', blank=True, default="")
    images = models.ManyToManyField(Gallery, blank=True, default="")
    order = models.IntegerField('Порядковый номер при отображении на сайте', default=100)
    is_show = models.BooleanField('Отображать на сайте?', default=True)




    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Текст для страницы'
        verbose_name_plural = 'Тексты для страниц'