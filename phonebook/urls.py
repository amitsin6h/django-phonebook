from django.conf.urls import url
from phonebook import views

urlpatterns = [
 
    url(r'^$', views.add_contact, name='add_contact'),
    
]
