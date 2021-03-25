from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.CreateUrl.as_view(), name = "generate-url"),
    path('<str:shortenedUrl>', views.RedirectToOriginal.as_view(), name = "generate-url"),
]