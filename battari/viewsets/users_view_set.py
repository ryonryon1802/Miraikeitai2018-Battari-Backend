import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from battari.constant import TOKEN_HEADER
from battari.data.models.response.users import UsersSerializer
from battari.domain.user.users import Users
from battari.models import User


class UsersViewSet(viewsets.ViewSet):
    def list(self, request):
        user = self.get_queryset()
        if user is None:
            return HttpResponse("Forbidden", status=403)

        users = Users(user.spotify_id)
        following = users.following()
        follower = users.follower()
        resp = [user.id, user.displayname, user.follows, user.icon, user.current_listening_track, user.comment, follower, following]
        resp_json = JSONRenderer().render(UsersSerializer(resp).data)

        serialized = UsersSerializer(data=resp_json)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)
        return HttpResponse(resp_json, status=200, content_type='application/json')
    #
    # @action(methods=["get"], detail=False)
    # def users(self, request):
    #     user = self.get_queryset()
    #     if user is None:
    #         return HttpResponse("Forbidden", status=403)
    #
    #     users = Users(user.spotify_id)
    #     following = users.following()
    #     follower = users.follower()
    #     resp = [user, following, follower]
    #     resp_json = JSONRenderer().render(UsersSerializer(resp).data)
    #
    #     serialized = UsersSerializer(data=resp_json)
    #     if not serialized.is_valid():
    #         return HttpResponse("Forbidden", status=403)
    #
    #     return HttpResponse(resp_json, status=200, content_type='application/json')

    def get_queryset(self):
        if TOKEN_HEADER not in self.request.META:
            return None
        try:
            token = self.request.META[TOKEN_HEADER]
            user = User.objects.get(battari_token=token)
            return user
        except ObjectDoesNotExist:
            return None
