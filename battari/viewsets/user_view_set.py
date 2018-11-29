import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets

from battari.constant import TOKEN_HEADER
from battari.data.models.response.user import UserSerializer
# from battari.domain.firebase.firebase import Firebase
from battari.models import User


class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        body = json.loads(request.body.decode())
        serialized = UserSerializer(data=body)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)

        data = serialized.validated_data
        print("test")
        return HttpResponse("OK", status=201)

    def get_queryset(self):
        if TOKEN_HEADER not in self.request.META:
            return None
        try:
            token = self.request.META[TOKEN_HEADER]
            user = User.objects.get(battari_token=token)
            return user
        except ObjectDoesNotExist:
            return None