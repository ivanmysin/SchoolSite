from django.shortcuts import render
import os
from .models import Organizators, Lectors, Partners, KeyDates, Faqs, TextPage, QualifyingTasks, ApplicationsForParticipation



def index(request):


    filenames = []
    for filename in os.listdir('/home/ivan/PycharmProjects/SchoolSite/school_site/main/static/main/images/home_slider'):
        if filename[-4:] != '.jpg': continue
        filenames.append(filename)


    data4render = {
        'text2title': 'О школе',
        'text2' : "Летняя школа \"Введение в нейробиологию внимания и памяти\" — ежегодное мероприятие. Цель школы - привлечение студентов в нейронауку. В рамках школы проходят лекции ведущих ученых, практические занятия и нейротурнир",
        'text1title' : 'Наша миссия',
        'text1' : ["Наша летняя научная школа предназначена для того, чтобы помочь студентам развить навыки научного исследования и критического мышления.",
                   "Мы стремимся предоставить студентам возможность погрузиться в мир науки и исследований, а также научиться работать в команде.",
                   "Наша летняя научная школа предлагает разнообразные курсы по различным областям научных знаний, включая физику, биологию и математику.",
                   "Мы считаем, что научное исследование имеет огромное значение для развития общества и будущего нашей планеты.",
                   "Мы стремимся создать дружественную и поддерживающую среду для всех участников, где они могут развивать свои таланты и достигать своих целей."],
        'filenames' : filenames,
    }
    return render(request, 'main/index.html', data4render)

def orgs(request):
    data4render = Organizators.objects.filter(is_show=True).order_by("order") #
    return render(request, 'main/orgs.html', {'orgs' : data4render})

def lectors(request):
    data4render = Lectors.objects.filter(is_show=True).order_by("order") #
    return render(request, 'main/lectors.html', {'lectors' : data4render})

def partners(request):
    data4render = Partners.objects.filter(is_show=True).order_by("order")
    return render(request, 'main/partners.html', {'partners' : data4render})



def dates(request):
    dates = KeyDates.objects.filter(is_show=True).order_by("date")
    return(render(request, 'main/dates.html', {'dates' : dates}))

def text(request):

    path = request.path.split(" ")[0][1:]


    if request.method == "POST" and path == "accepted_application":

        accepted_data = {}
        qualifying_answers = ""
        for key, val in request.POST.items():

            if key.find("answer_for_task_") != -1:
                qualifying_answers = key + ":  " + qualifying_answers + "\n################\n" + val

            elif key == "csrfmiddlewaretoken":
                continue
            else:
                accepted_data[key] = val


        accepted_data["qualifying_answers"] = qualifying_answers
        accepted_form = ApplicationsForParticipation(**accepted_data)


        # if accepted_form.is_valid():
        accepted_form.save()

        texts_page = [{
            "title" : "Форма успешно отправлена!",
            "text" : "",
        },]
    else:
        texts_page = TextPage.objects.filter(is_show=True, page=path).order_by("order")


    data = {
        "texts_page" : texts_page,
    }
    return (render(request, 'main/text.html', data))



# def history(request):
#
#     data = {
#         'tiltes' : ['Школа 2023', 'Школа 2022', 'Школа 2021', 'Школа 2018'],
#         'schools' : [],
#     }
#
#     return (render(request, 'main/history.html', data))

def faqs(request):
    faqs = Faqs.objects.filter(is_show=True).order_by("order")
    data = {
        'faqs' : faqs,
    }
    return (render(request, 'main/faqs.html', data))

def send_application(request):
    tasks = QualifyingTasks.objects.filter(is_show=True).order_by("order")
    data = {
        'tasks': tasks,
    }
    return (render(request, 'main/send_application.html', data))