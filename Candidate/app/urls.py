from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.CandidateListAPIView.as_view(), name='candidate-list'),
    path('candidates/<int:pk>/', views.CandidateDetailAPIView.as_view(), name='candidate-detail'),

    path('', views.candidate_list, name='candidate_list'),
    path('candidate/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidate/new/', views.candidate_new, name='candidate_new'),
    path('candidate/<int:pk>/edit/', views.candidate_edit, name='candidate_edit'),
    path('candidate/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),
]
