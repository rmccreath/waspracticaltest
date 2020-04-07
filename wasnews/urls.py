from django.urls import path
from . import views

app_name = 'wasnews'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:newsstory_id>/', views.news, name='news'),
]
