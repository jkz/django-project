from django.conf.urls import url, patterns, include

from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', lambda request: HttpResponse('Great succes')),
)
