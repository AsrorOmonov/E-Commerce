from django.urls import path

from home.views import index
from my_admin.views import detail, create, edit, delete
app_name = 'my_admin'
urlpatterns = [
    path('', index),
    path('<int:pk>/', detail),
    path('create/', create),
    path('<int:pk>/edit/', edit),
    path('<int:pk>/delete/', delete),
]
