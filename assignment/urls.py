from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_admin.views import index, detail, create, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_admin/', index),
    path('my_admin/<int:pk>/', detail),
    path('my_admin/create/', create),
    path('my_admin/<int:pk>/edit/', edit),
    path('my_admin/<int:pk>/delete/', delete),
    path('', include('home.urls', 'home'))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
