from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = 'about'),
    path('projects/', views.projects, name = 'projects'),
    path('projects/<int:cat>/', views.projects_by_id, name = 'projects_ids'),
]
