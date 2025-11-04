from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.membersView),
    path('members/<int:pk>/', views.memberDetailView),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('userprofiles/', views.userProfilesView),
    path('userprofiles/<int:pk>/', views.userProfileDetailView),
]