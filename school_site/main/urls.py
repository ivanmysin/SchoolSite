from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db.utils import OperationalError

from .models import SiteMenu

url_menu = []
try:
    menu_q = SiteMenu.objects.filter(is_show_top=True) | SiteMenu.objects.filter(is_show_left=True)
    for menu in menu_q.values():
        url_menu.append( path(menu["link"], views.TextPageView.as_view(), name=menu["link"]) )
except OperationalError:
    pass

print(url_menu)


urlpatterns = ([
    path("", views.TextPageView.as_view(), name='home'),
    path("dates", views.DatesView.as_view(), name='dates'),
    path("orgs", views.ListPageView.as_view(), name='orgs'),
    path("lectors", views.ListPageView.as_view(), name='lectors'),
    path("partners", views.ListPageView.as_view(), name='partners'),
    # path("lodging", views.TextPageView.as_view(), name='lodging'),
    # path("payment", views.TextPageView.as_view(), name='payment'),
    path("contacts", views.TextPageView.as_view(), name='contacts'),
    #path("history", views.TextPageView.as_view(), name='history'),
    path("faqs", views.FAQView.as_view(), name='faqs'),

    path("send_application", views.SendPageView.as_view(), name='send_application'),
    #path("accepted_application", views.text, name='accepted_application'),
    path("accepted_application", views.TextPageView.as_view(), name='accepted_application'),

] + url_menu + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
