from django.conf.urls import include, url
# from django.contrib import admin
from .settings import BASE_URL

urlpatterns = [
    url(r'^{}/'.format(BASE_URL),
        include([
            url(r'^', include('rest.urls', 'rest')),
        ])),
]
