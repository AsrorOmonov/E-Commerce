from django.urls import path
from home.views import index, detail, OutfitListView

app_name = 'home'

urlpatterns = [
    path('', OutfitListView.as_view()),
    path('<int:pk>/', detail)
]
