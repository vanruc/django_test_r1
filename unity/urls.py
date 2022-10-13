from django.urls import path, include
from . import views

app_name = 'unity'
urlpatterns = [
    path('leads/list', views.lead_listing, name='lead_listing'),
]
