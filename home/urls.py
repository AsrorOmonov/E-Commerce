from django.urls import path

from home.views import index, detail

app_name = 'home'

urlpatterns = [
    path('', index),
    path('<int:pk>/', detail)
]
