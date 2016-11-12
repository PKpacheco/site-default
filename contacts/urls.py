from django.conf.urls import include, url

from .views import list_contact

urlpatterns = [

    url(r'^contato/', list_contact, name='list_contact'),

]
