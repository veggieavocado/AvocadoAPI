from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from services.models import (
    Sentence,
    Text,
    Word,
    State,
    )
from services.serializers import (
    SentenceSerializer,
    TextSerializer,
    WordSerializer,
    StateSerializer,
    )
from utils.paginations import StandardResultPagination

# sentence view GET POST
class SentenceAPIView(generics.ListCreateAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Sentence.objects.all().order_by('id')
        owner_by = self.request.GET.get('owner')
        userid_by = self.request.GET.get('userid')
        source_by = self.request.GET.get('source')
        role_by = self.request.GET.get('role')
        detail_role_by = self.request.GET.get('detail_role')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if userid_by:
            queryset = queryset.filter(userid=userid_by)
        if owner_by and userid_by:
            queryset = queryset.filter(owner=owner_by).filter(userid=userid_by)
        if source_by:
            queryset = queryset.filter(source=source_by)
        if role_by:
            queryset = queryset.filter(role=role_by)
        if detail_role_by:
            queryset = queryset.filter(detail_role=detail_role_by)

        return queryset

# sentence view PUT DELETE
class SentenceDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#Text Views GET POST
class TextAPIView(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Text.objects.all().order_by('id')
        owner_by = self.request.GET.get('owner')
        userid_by = self.request.GET.get('userid')
        type_by = self.request.GET.get('type')
        source_by = self.request.GET.get('source')
        cartegory_by = self.request.GET.get('cartegory')
        title_by = self.request.GET.get('title')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if userid_by:
            queryset = queryset.filter(userid=userid_by)
        if owner_by and userid_by:
            queryset = queryset.filter(owner=owner_by).filter(userid=userid_by)
        if type_by:
            queryset = queryset.filter(type=type_by)
        if source_by:
            queryset = queryset.filter(source=category_by)
        if title_by:
            queryset = queryset.filter(title=title_by)

        return queryset

# TEXT view PUT DELETE
class TextDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

# Word view GET POST
class WordAPIView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Word.objects.all().order_by('id')
        owner_by = self.request.GET.get('owner')
        userid_by = self.request.GET.get('userid')
        source_by = self.request.GET.get('source')
        role_by = self.request.GET.get('role')
        detail_role_by = self.request.GET.get('detail_role')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if userid_by:
            queryset = queryset.filter(userid=userid_by)
        if owner_by and userid_by:
            queryset = queryset.filter(owner=owner_by).filter(userid=userid_by)
        if source_by:
            queryset = queryset.filter(source=source_by)
        if role_by:
            queryset = queryset.filter(role=role_by)
        if detail_role_by:
            queryset = queryset.filter(detail_role=detail_role_by)

        return queryset

# Word view PUT DELETE
class WordDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


# State view GET POST
class StateAPIView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]


# State view PUT DELETE
class StateDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
