from django.shortcuts import render
import os
from .models import Organizators, Lectors, Partners, \
        KeyDates, Faqs, TextPage, QualifyingTasks,\
        ApplicationsForParticipation, SiteMenu, QualifyingAnswers,\
        FormatsOfParticipation, Contacts, Gallery, CommonSettings
from django.views.generic.base import ContextMixin
from django.views.generic import TemplateView
import smtplib
from email.message import EmailMessage
from school_site import myconfig
from django.conf import settings
import timeout_decorator


class NavView(ContextMixin):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        common_settings = CommonSettings.objects.all()#.values()
        for common_setting in common_settings:
            context[common_setting.setting_name] = common_setting.setting_value



        context["nav_links_top"] = SiteMenu.objects.filter(is_show_top=True).order_by("order").values()

        for nav_el in context["nav_links_top"]:
            if nav_el["link"] == "":
                nav_el["link"] = "home"

        context["nav_links_left"] = SiteMenu.objects.filter(is_show_left=True).order_by("order").values()
        for nav_el in context["nav_links_left"]:
            if nav_el["link"] == "":
                nav_el["link"] = "home"

        context["debug"] = settings.DEBUG

        path = self.request.path.split(" ")[0][1:]

        if path == "":
            path = "home"
        self.active_menu = SiteMenu.objects.filter(link=path)[0]
        context["title"] = self.active_menu.name

        return context

class ContactsView(ContextMixin):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["contacts"] = Contacts.objects.filter(is_show=True).order_by("order")
        return context

class Galleries(ContextMixin):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["header_gallery"] = Gallery.objects.filter(is_show_in_header=True).order_by("order")
        context["common_gallery"] = Gallery.objects.filter(is_show_in_common_gallery=True).order_by("order")
        return context

class TextPageView(TemplateView, NavView, ContactsView, Galleries):
    template_name = "main/text.html"

    # other methods and stuffs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


        #menu = SiteMenu.objects.filter(link=path)[0]
        texts_page_query_set = TextPage.objects.filter(is_show=True, page=self.active_menu).order_by("order")
        texts_page = list( texts_page_query_set.values() )
        for tp_idx, tpqs in enumerate(texts_page_query_set):
            texts_page[tp_idx]["images"] = tpqs.images.all().values()

        context["texts_page"] = texts_page
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        context["texts_page"] = self.process_participation_form()
        return self.render_to_response(context)

    def process_participation_form(self):

        path = self.request.path.split(" ")[0][1:]

        qualifying_answers = []
        accepted_data = {}

        if self.request.method == "POST" and path == "accepted_application":
            try:
                for key, val in self.request.POST.items():
                    if key.find("answer_for_task_") != -1:
                        task_id = int(key.split("_")[-1])
                        qualifying_answers.append({"task_id": task_id,
                                                   "answer": val})  # = key + ":  " + qualifying_answers + "\n################\n" + val

                    elif key == "csrfmiddlewaretoken":
                        continue
                    else:
                        accepted_data[key] = val

                jointed_answers = ""
                task_number = 1
                for answer in sorted(qualifying_answers, key=lambda d: d['task_id']):
                    jointed_answers += "Задача № {} \n {} \n#######################\n".format(task_number, answer["answer"])
                    task_number += 1

                accepted_data["qualifying_answers"] = jointed_answers

                accepted_form = ApplicationsForParticipation(**accepted_data)
                accepted_form.save()

                for answer in qualifying_answers:
                    answer_dict = {
                        "participant_id": accepted_form,
                        "task_id": QualifyingTasks.objects.get(id=answer["task_id"]),
                        "answer": answer["answer"],
                    }
                    ans = QualifyingAnswers(**answer_dict)
                    ans.save()

                send_email(accepted_data)
                texts_page = [{
                    "title": "Ваша заявка успешно отправлена!",
                    "text": "Подтверждение отправлено на почту {}. Если письмо не пришло, проверьте спам.".format(accepted_data["email"]),
                }, ]

            except:
                texts_page = [{
                    "title": "Форма содержит ошибки!",
                    "text": "Попробуйте заполнить форму еще раз",
                }, ]

        return texts_page




class ListPageView(TemplateView, NavView, ContactsView, Galleries):
    template_name = "main/list_page.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        path = self.request.path.split(" ")[0][1:]
        if path == "lectors":
            context["title_of_list"] = "Лекторы"
            data4render = Lectors.objects.filter(is_show=True).order_by("order").values()
        elif path == "orgs":
            context["title_of_list"] = "Оргкомитет Школы"
            data4render = Organizators.objects.filter(is_show=True).order_by("order").values()
        elif path == "partners":
            context["title_of_list"] = "Партнеры и спонсоры"
            data4render = Partners.objects.filter(is_show=True).order_by("order").values()

        for data in data4render:
            if os.path.isfile(data["path_to_photo"]):
                img_file = os.path.split(data["path_to_photo"])[-1]
            else:
                img_file = "static/main/images/no_photo.jpeg"
                data["path_to_photo"] = img_file

            if path == "orgs":
                data["strong"] = "{} {} {}".format(data["surname"], data["name"], data["patronymic"])
                data["subscript"] = data["role"]
            elif path == "lectors":
                data["strong"] = "{} {} {}".format(data["surname"], data["name"], data["patronymic"])
                data["subscript"] = "{}, {}".format(data["degree"], data["affilation"])
            elif path == "partners":
                data["strong"] = data["organization_name"]
                data["subscript"] = data["organization_description"]

            #data["subscript"] = "{} {} {}".format(data["surname"], data["name"], data["patronymic"])
        context["persons"] = data4render
        return context

class SendPageView(TemplateView, NavView, ContactsView, Galleries):
    template_name = "main/send_application.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tasks"] = QualifyingTasks.objects.filter(is_show=True).order_by("order")
        context["formats"] = FormatsOfParticipation.objects.filter(is_show=True)

        return context

class DatesView(TemplateView, NavView, ContactsView, Galleries):
    template_name = "main/dates.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["dates"] = KeyDates.objects.filter(is_show=True).order_by("date")
        return context

class FAQView(TemplateView, NavView, ContactsView, Galleries):
    template_name = "main/faqs.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["faqs"] = Faqs.objects.filter(is_show=True).order_by("order")
        # context["title_of_page"] = "Частые вопросы"
        return context

@timeout_decorator.timeout(15)
def send_email(form_data):
    sender_email_address = myconfig.sender_email_address
    receiver_email_address = form_data["email"]
    email_smtp = myconfig.email_smtp
    email_password = myconfig.email_password

    # create an email message object
    email_subject = 'Оргкомитет летней научной школы "Введение в нейробиологию внимания и памяти"'
    message = EmailMessage()

    # configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # set email body text
    with open("./main/templates/main/Confirmation_Letter.html", mode="r") as f:
        email_body_template = f.read()
    email_body = email_body_template.format(name=form_data["name"], patronymic=form_data["patronymic"])
    message.set_content(email_body, subtype='html')

    # set smtp server and port
    server = smtplib.SMTP(email_smtp, '587')
    # identify this client to the SMTP server
    server.ehlo()
    # secure the SMTP connection
    server.starttls()

    # login to email account
    server.login(sender_email_address, email_password)
    # send email
    server.send_message(message)
    # close connection to server
    server.quit()
    return
