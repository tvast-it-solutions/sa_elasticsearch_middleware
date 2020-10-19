from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status
import requests
import json

DESTIONATION_URL = settings.DESTINATION_HOST


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def root_view(request):
    try:
        partial_url = request.get_full_path()
        request_method = request.method
        final_url = '{}{}'.format(DESTIONATION_URL, partial_url)
        request_headers = {'Content-Type': 'application/json'}

        if request_method == 'GET':
            response_body = requests.get(
                final_url,
                headers=request_headers,
            ).json()
        else:
            request_body = json.dumps((request.body).decode('utf-8'))
            response_body = requests.post(
                final_url,
                headers=request_headers,
                data=request_body
            ).json()

        response_body = json.dumps(response_body)
        return HttpResponse(response_body)

    except Exception as ex:
        return HttpResponse({'error': ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
