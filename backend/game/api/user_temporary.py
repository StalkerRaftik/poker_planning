from uuid import uuid4

from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from game.api.api_permissions import IsNotAuthenticatedPermission


class TemporaryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class TemporaryUserView(APIView):
    permission_classes = [IsNotAuthenticatedPermission]
    serializer_class = TemporaryUserSerializer

    @swagger_auto_schema(
        request_body=TemporaryUserSerializer,
        responses={201: TokenSerializer()}
    )
    def post(self, request):
        serializer = TemporaryUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        temporary_user = User.objects.create(username=serializer.validated_data['username'], password=uuid4().hex)
        token = Token.objects.create(user=temporary_user)

        return Response(
            data=TokenSerializer(token).data,
            status=status.HTTP_201_CREATED
        )
