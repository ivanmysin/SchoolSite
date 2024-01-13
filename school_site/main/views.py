from django.shortcuts import render
import os
from .models import Organizators, Lectors, Partners, \
        KeyDates, Faqs, TextPage, QualifyingTasks,\
        ApplicationsForParticipation, SiteMenu, QualifyingAnswers,\
        FormatsOfParticipation, Contacts
#from school_site.main.templates.forms import ApplicationsForParticipationForm, QualifyingAnswersForm
from django.views.generic.base import ContextMixin
from django.views.generic import View, TemplateView

class NavView(ContextMixin):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["nav_links"] = SiteMenu.objects.filter(is_show_top=True).order_by("order") | SiteMenu.objects.filter(is_show_left=True).order_by("order")
        return context

class ContactsView(ContextMixin):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["contacts"] = Contacts.objects.filter(is_show=True).order_by("order")
        return context
class TextPageView(TemplateView, NavView, ContactsView):
    template_name = "main/text.html"

    # other methods and stuffs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        path = self.request.path.split(" ")[0][1:]
        texts_page = TextPage.objects.filter(is_show=True, page=path).order_by("order")

        context["texts_page"] = texts_page
        return context



class ListPageView(TemplateView, NavView, ContactsView):
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

class SendPageView(TemplateView, NavView, ContactsView):
    template_name = "main/send_application.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tasks"] = QualifyingTasks.objects.filter(is_show=True).order_by("order")
        context["formats"] = FormatsOfParticipation.objects.filter(is_show=True)

        return context

# def send_application(request):
#
#     data = {
#         'tasks': tasks,
#     }

# def orgs(request):
#     data4render = Organizators.objects.filter(is_show=True).order_by("order").values()
#
#     for data in data4render:
#         if os.path.isfile(data["path_to_photo"]):
#             img_file = os.path.split(data["path_to_photo"])[-1]
#         else:
#             img_file = "no_photo.jpeg"
#         data["path_to_photo"] = img_file
#     return render(request, 'main/orgs.html', {'orgs' : data4render})
#
# def lectors(request):
#     data4render = Lectors.objects.filter(is_show=True).order_by("order").values()
#     for data in data4render:
#         if os.path.isfile(data["path_to_photo"]):
#             img_file = os.path.split(data["path_to_photo"])[-1]
#         else:
#             img_file = "no_photo.jpeg"
#         data["path_to_photo"] = img_file
#     return render(request, 'main/lectors.html', {'lectors' : data4render})
#
# def partners(request):
#     data4render = Partners.objects.filter(is_show=True).order_by("order").values()
#     for data in data4render:
#         if os.path.isfile(data["path_to_photo"]):
#             img_file = os.path.split(data["path_to_photo"])[-1]
#         else:
#             img_file = "no_photo.jpeg"
#         data["path_to_photo"] = img_file
#     return render(request, 'main/partners.html', {'partners' : data4render})



def dates(request):
    dates = KeyDates.objects.filter(is_show=True).order_by("date")
    return(render(request, 'main/dates.html', {'dates' : dates}))

def text(request):


    path = request.path.split(" ")[0][1:]

    answers = []

    qualifying_answers = []
    accepted_data = {}

    if request.method == "POST" and path == "accepted_application":
        try:
            for key, val in request.POST.items():
                if key.find("answer_for_task_") != -1:
                    task_id = int(key.split("_")[-1])
                    qualifying_answers.append({"task_id" : task_id, "answer" : val}) # = key + ":  " + qualifying_answers + "\n################\n" + val

                elif key == "csrfmiddlewaretoken":
                    continue
                else:
                    accepted_data[key] = val

            jointed_answers = ""
            task_number = 1
            for answer in sorted(qualifying_answers, key=lambda d: d['task_id']):
                jointed_answers += "Задача № {} \n {} \n\n".format(task_number, answer["answer"])
                task_number += 1

            accepted_data["qualifying_answers"] = jointed_answers
            accepted_form = ApplicationsForParticipation(**accepted_data)
            accepted_form.save()

            for answer in qualifying_answers:
                answer_dict = {
                    "participant_id" : accepted_form,
                    "task_id": QualifyingTasks.objects.get(id=answer["task_id"]),
                    "answer" : answer["answer"],
                }
                ans = QualifyingAnswers(**answer_dict)
                ans.save()



            texts_page = [{
                "title" : "Ваша заявка успешно отправлена!",
                "text" : "Подтверждение отправлено на почту {}".format(accepted_data["email"]),
            },]

        except ZeroDivisionError:
            texts_page = [{
                "title" : "Форма содержит ошибки!",
                "text" : "",
            },]
    data = {
        "texts_page" : texts_page,
        "menu" : [],
    }
    return (render(request, 'main/text.html', data))



def faqs(request):
    faqs = Faqs.objects.filter(is_show=True).order_by("order")
    data = {
        'faqs' : faqs,
    }
    return (render(request, 'main/faqs.html', data))

# def send_application(request):
#     tasks = QualifyingTasks.objects.filter(is_show=True).order_by("order")
#     data = {
#         'tasks': tasks,
#     }
#     return (render(request, 'main/send_application.html', data))