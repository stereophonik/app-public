from django.urls import path
from project.app import views

urlpatterns = [
    path('outcomes/', views.outcome_list)
]
