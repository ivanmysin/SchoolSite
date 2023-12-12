from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("dates", views.dates, name='dates'),
    path("orgs", views.orgs, name='orgs'),
    path("lectors", views.lectors, name='lectors'),
    path("partners", views.partners, name='partners'),
    path("lodging", views.text, name='lodging'),
    path("payment", views.text, name='payment'),
    path("contacts", views.text, name='contacts'),
    path("send_application", views.text, name='send_application'),

    path("history", views.history, name='history'),
    path("faqs", views.faqs, name='faqs'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
