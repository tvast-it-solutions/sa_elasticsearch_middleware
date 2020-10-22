from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import json
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


schema_view = get_schema_view(
    openapi.Info(
        title="Sentiment Analysis Middleware API",
        default_version='v1',
        description="API docs for middleware between elasticsearch and web client",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@api_view(['POST'])
@csrf_exempt
def login_view(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(
            username=username,
            password=password,
        )
        if user is None:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'key': token.key,
                    'email': user.email,
                    'userType': user.userType,
                },
                status=status.HTTP_200_OK,
            )

    except Exception as ex:
        return HttpResponse({'error': ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('auth/login/', login_view),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
]
