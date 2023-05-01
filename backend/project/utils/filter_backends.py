from rest_framework.filters import BaseFilterBackend


class BaseOrderingFilterBackend(BaseFilterBackend):
    """
    A base class from which all filter backend classes should inherit.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.order_by('id')
