from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.membersView),
    path('members/<int:pk>/', views.memberDetailView),
]