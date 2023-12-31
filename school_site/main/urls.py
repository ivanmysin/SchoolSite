from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.text, name='home'), # views.index
    path("dates", views.dates, name='dates'),
    path("orgs", views.orgs, name='orgs'),
    path("lectors", views.lectors, name='lectors'),
    path("partners", views.partners, name='partners'),
    path("lodging", views.text, name='lodging'),
    path("payment", views.text, name='payment'),
    path("contacts", views.text, name='contacts'),
    path("history", views.text, name='history'),
    path("faqs", views.faqs, name='faqs'),

    path("send_application", views.send_application, name='send_application'),
    path("accepted_application", views.text, name='accepted_application'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
