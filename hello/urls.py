from django.conf.urls import  include, url
from hello.views import hello,current_datetime,hours_ahead

urlpatterns = [
    url('^hello/$',hello),
    url('^time/$',current_datetime),
    url('^time/plus/(\d{1,2})/$',hours_ahead),
]
