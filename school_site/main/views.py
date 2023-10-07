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
            "surname" : 'Фамилия Отчество',
            "role" : 'За что человек отвечает',
            "photo" : '',
        }

        if request.path.find('lectors') != -1:
            org['role'] = 'Регалии и место работы'

        if request.path.find('partners') != -1:
            org['role'] = ''
            org['name'] = 'Название компании'
            org['surname'] = 'Опрсание компании, чем она занимается'



        data4render.append(org)



    return render(request, 'main/orgs.html', {'orgs' : data4render})

def dates(request):
    dates = {
        'dates' : ['01.06.2023 - Срок полачи заявки', '20.06.2023 - Объявление результатов отбора', '06.08.2023 - 18.08.2023 - Проведение школы'],
    }
    return(render(request, 'main/dates.html', dates))

def text(request):

    path = request.path.split(" ")[0][1:]
    title = 'Заголовок страницы'
    text = 'Содержание страницы'

    if path == 'send_application':
        title = 'Отравить заявку'
        text = 'Срок отправки заявок окончек'

    elif path == 'contacts':
        title = 'Наши контакты'
        text = """
         Почта hippicampus.psn@gmail.com  
         Сообщество в ВК vk.com/labson
        """
    elif path == 'payment':
        title = 'Оргвзнос'
        text = """ Участие в школе стоит 4000  руб.
         Оргвзнос включает проживание в общежитии, кофе-брейки, фуршет по поводу открытия и закрытия школы"""

    elif path == 'lodging':
        title = 'Проживание в Пущино'
        text = """ Участникам на время школы предоставляется место в студенческом общежитии биотехнологического факультета МГУ"""

    data = {
        'title' : title,
        'text' : text,
    }
    return (render(request, 'main/text.html', data))



def history(request):

    data = {
        'tiltes' : ['Школа 2023', 'Школа 2022', 'Школа 2021', 'Школа 2018'],
        'schools' : [],
    }

    return (render(request, 'main/history.html', data))

def faqs(request):
    questions = ['Кто может участвовать?', 'Что взять с собой?', 'Куда приезжать?', 'Где проходит школа?', 'Сколько это стоит?'],
    answers = ['Заявку может подать любой в совершенно летний', 'Ноутбук, купальные пренадлежности, хорошее настроение', 'Пущино, В 20А', 'Пущино, Институтская 3',  'ПОбробности в разделе Оргвзнос'],

    faqs = zip(questions, answers)
    data = {
        'faqs' : faqs,
    }
    return (render(request, 'main/faqs.html', data))