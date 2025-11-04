from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    emp_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.emp_name} ({self.emp_id})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    is_admin = models.BooleanField(default=False)
    company = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="users",  # Allows company.users.all() to retrieve all users
        verbose_name="Company",
        help_text="The company this user belongs to."
    )
    def __str__(self):
        return f"Profile of {self.is_admin}"