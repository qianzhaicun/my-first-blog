from django.conf.urls import *
import app.views

urlpatterns = [
    url(r'^latest/$', app.views.latest_books),
    ]
    
  
