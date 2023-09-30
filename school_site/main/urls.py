from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("about_us", views.about, name='about_us'),
    path("dates", views.about, name='dates'),
    path("orgs", views.about, name='orgs'),
    path("lodging", views.about, name='lodging'),
    path("payment", views.about, name='payment'),
    path("contacts", views.about, name='contacts'),
    path("send_application", views.about, name='send_application'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
