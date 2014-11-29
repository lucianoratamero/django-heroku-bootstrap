from django.conf.urls import patterns, include, url

from app.views import *

urlpatterns = patterns('app.views',
    url(r'^$', IndexView.as_view(), name="index"),
)
