from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from core.models import Candidate


class CandidateInfo(APIView):
        
    def get(self, request, *args, **kwargs):
        candidate_id = kwargs.pop('candidate_id', None)
        candidate = Candidate.objects.get(id=candidate_id)
        response_data = {
            "name": candidate.name,
            "email": candidate.email,
            "job_expectations": candidate.job_expectations
        }
        return Response(data=response_data, status=HTTP_200_OK)
