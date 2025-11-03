from django.urls import path
from . import views

urlpatterns = [
     # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),

    # Skills
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/<int:pk>/', views.skill_detail, name='skill_detail'),

    # History
    path('history/', views.history_list, name='history_list'),
    path('history/<int:pk>/', views.history_detail, name='history_detail'),

    # API pour React (POST seulement)
    path('contact/', views.api_create_contact, name='api_create_contact'),

    # Backend Django pour affichage et suppression
    path('contact/list/', views.contact_list, name='listContact'),
    path('contact/<int:pk>/delete/', views.delete_contact, name='deleteContact'),
]