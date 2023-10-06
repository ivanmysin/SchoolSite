from django.shortcuts import render
import os
# Create your views here.


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
    data4render = []

    for i in range(15):
        org = {
            "name" : 'Имя',
            "surname" : 'Фамилия',
            "role" : 'За что человек отвечает',
            "photo" : '',
        }
        data4render.append(org)


    return render(request, 'main/orgs.html', {'orgs' : data4render})
