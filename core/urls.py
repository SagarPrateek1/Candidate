from django.urls import path

from core.views import CandidateInfo

urlpatterns = [
    path('details/<str:candidate_id>', CandidateInfo.as_view(), name="candidate_info_view"),

]
