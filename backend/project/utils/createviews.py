from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

mixins = {
    'LIST': mixins.ListModelMixin,
    'CREATE': mixins.CreateModelMixin,
    'DETAIL': mixins.RetrieveModelMixin,
    'UPDATE': mixins.UpdateModelMixin,
    'DELETE': mixins.DestroyModelMixin,
}


class SetMethodsMetaClass(type):
    """
    Base ViewSet metaclass.
    Provides actions mixins via `methods` list attribute.
    ex.: methods = ('LIST', 'CREATE', 'DELETE')
    """
    @staticmethod
    def get_additional_bases(attrs):
        methods = attrs.get('methods', mixins.keys())
        additional_bases = []
        for method in methods:
            if method not in mixins:
                continue
            additional_bases.append(mixins[method])
        additional_bases.append(GenericViewSet)

        return additional_bases

    def __new__(mcs, name, bases, attrs):
        return super().__new__(
            mcs,
            name,
            (
                *bases,
                *mcs.get_additional_bases(attrs)
            ),
            attrs,
        )


class DependSerializerViewMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset.
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        custom_serializer = getattr(self, f'{self.action}_serializer_class', None)
        if custom_serializer:
            return custom_serializer
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class
