from rest_framework import serializers
from rest_framework import viewsets, mixins

from game.models.game import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('issue',)


class VoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(game_member=self.request.user)
