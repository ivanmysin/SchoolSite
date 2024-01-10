from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .models import SiteMenu

menu_q = SiteMenu.objects.filter(is_show_top=True) | SiteMenu.objects.filter(is_show_left=True)

url_menu = []
for menu in menu_q.values():
    url_menu.append( path(menu["link"], views.TextPageView.as_view(), name=menu["link"]) )


urlpatterns = ([
    path("", views.TextPageView.as_view(), name='home'),
    path("dates", views.dates, name='dates'),
    path("orgs", views.orgs, name='orgs'),
    path("lectors", views.lectors, name='lectors'),
    path("partners", views.partners, name='partners'),
    path("lodging", views.TextPageView.as_view(), name='lodging'),
    path("payment", views.TextPageView.as_view(), name='payment'),
    path("contacts", views.TextPageView.as_view(), name='contacts'),
    path("history", views.TextPageView.as_view(), name='history'),
    path("faqs", views.faqs, name='faqs'),

    path("send_application", views.send_application, name='send_application'),
    path("accepted_application", views.text, name='accepted_application'),

] + url_menu + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
