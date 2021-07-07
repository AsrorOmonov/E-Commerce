from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_admin.views import index, detail, create, edit, delete, AdminListView, OutfitDetailView, OutfitCreateView, \
    OutfitUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', 'home')),
    ############## my_admin    #################
    path('my_admin/', AdminListView.as_view()),
    path('my_admin/<int:pk>/', OutfitDetailView.as_view()),
    path('my_admin/create/', OutfitCreateView.as_view()),
    path('my_admin/<int:pk>/edit/', OutfitUpdateView.as_view()),
    path('my_admin/<int:pk>/delete/', delete),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
