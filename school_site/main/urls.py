from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("dates", views.index, name='dates'),
    path("orgs", views.orgs, name='orgs'),
    path("lodging", views.index, name='lodging'),
    path("payment", views.index, name='payment'),
    path("contacts", views.index, name='contacts'),
    path("send_application", views.index, name='send_application'),
    path("partners", views.index, name='partners'),
    path("history", views.index, name='history'),
    path("faqs", views.index, name='faqs'),
    path("lectors", views.index, name='lectors'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
