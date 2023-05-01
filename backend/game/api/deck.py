from django.db.models import Q
from rest_framework import serializers, viewsets, status, permissions, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game.api.api_permissions import OwnerPermission
from game.models import Deck, DeckCard
from django_filters.rest_framework import OrderingFilter


class DeckCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckCard
        fields = ('value',)


class DeckSerializer(serializers.ModelSerializer):
    cards = DeckCardSerializer(many=True)

    class Meta:
        model = Deck
        fields = ('name', 'cards')


class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    permission_classes = (IsAuthenticated, OwnerPermission('creator'))

    def get_queryset(self):
        return Deck.objects.filter(Q(creator=self.request.user) | Q(is_global_deck=True))

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=['post'], serializer_class=DeckCardSerializer)
    def create_deck_card(self, request, *args, **kwargs):
        deck = self.get_object()
        if deck.cards.count() == 10:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        DeckCard.objects.create(**serializer.validated_data, deck=deck)
        return Response(status=status.HTTP_201_CREATED)


class DeckCardViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    class DeckCardPermission(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.deck.creator == request.user

    serializer_class = DeckCardSerializer
    permission_classes = (IsAuthenticated, DeckCardPermission)
