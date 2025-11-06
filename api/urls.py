from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')
router.register('blogs', views.BlogViewset, basename='blog')
router.register('comments', views.CommentViewset, basename='comment')
router.register('reactions', views.ReactionViewset, basename='reaction')

urlpatterns = [
    path('members/', views.membersView),
    path('members/<int:pk>/', views.memberDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('userprofiles/', views.userProfilesView),
    path('userprofiles/<int:pk>/', views.userProfileDetailView),
] + router.urls