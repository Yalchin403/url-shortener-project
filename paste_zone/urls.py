from django.urls import path
from . import views

app_name = 'paste_zone'
urlpatterns = [
    path('zone', views.CreatePaste.as_view(), name = "generate-paste"),
    path('zone/delete/<str:pk>', views.DeletePaste.as_view(), name = "delete-paste"),
    path('zone/<str:slug>', views.DetailView.as_view(), name = "detail-url"),
]
