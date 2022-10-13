from django.urls import path
from . import views

app_name = 'unity'
urlpatterns = [
    path('leads/subscribe', views.LeadsSubscribe.as_view(),
         name='leads_subscribe'),
]
