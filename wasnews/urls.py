from django.urls import path
from wasnews import views

app_name = 'wasnews'

urlpatterns = [
    path('', views.index, name='index'),
]