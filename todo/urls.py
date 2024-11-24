from django.urls import path
from .views import task_create

urlpatterns = [
    path('', task_create)
]
