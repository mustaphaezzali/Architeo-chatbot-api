from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiCandidat import views

urlpatterns = [
    path('candidats/', views.CandidatList.as_view()),
    path('candidats/<int:pk>', views.CandidatDetail.as_view()),
    path('recruteurs/', views.RecruteurList.as_view()),
    path('recruteurs/<int:pk>', views.RecruteurDetail.as_view()),
    path('partenaires/', views.PartenaireList.as_view()),
    path('partenaires/<int:pk>', views.PartenaireDetail.as_view()),
    path('clients/', views.CandidatList.as_view()),
    path('clients/<int:pk>', views.CandidatDetail.as_view()),
    path('offres/', views.OffreList.as_view()),
    path('offres/<int:pk>', views.OffreDetail.as_view()),
    path('meetings/', views.MeetingList.as_view()),
    path('meetings/<int:pk>', views.MeetingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)