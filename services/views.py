from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from services.models import (
    Sentence,
    Text,
    Word,
    State,
    Structure,
    )

from services.serializers import (
    SentenceSerializer,
    TextSerializer,
    WordSerializer,
    StateSerializer,
    StructureSerializer,
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
        username_by = self.request.GET.get('username')
        source_by = self.request.GET.get('source')
        role_by = self.request.GET.get('role')
        detail_role_by = self.request.GET.get('detail_role')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if username_by:
            queryset = queryset.filter(username=username_by)
        if owner_by and username_by:
            queryset = queryset.filter(owner=owner_by).filter(username=username_by)
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
        username_by = self.request.GET.get('username')
        type_by = self.request.GET.get('type')
        source_by = self.request.GET.get('source')
        cartegory_by = self.request.GET.get('cartegory')
        title_by = self.request.GET.get('title')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if username_by:
            queryset = queryset.filter(username=username_by)
        if owner_by and username_by:
            queryset = queryset.filter(owner=owner_by).filter(username=username_by)
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
        username_by = self.request.GET.get('username')
        source_by = self.request.GET.get('source')
        role_by = self.request.GET.get('role')
        detail_role_by = self.request.GET.get('detail_role')

        if owner_by:
            queryset = queryset.filter(owner=owner_by)
        if username_by:
            queryset = queryset.filter(username=username_by)
        if owner_by and username_by:
            queryset = queryset.filter(owner=owner_by).filter(username=username_by)
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
    queryset = State.objects.all().order_by('-id')
    serializer_class = StateSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

# State view PUT DELETE
class StateDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

# PPT view GET
class UserPptView(generics.ListAPIView):
    queryset = Text.objects.filter(type='PPT')
    serializer_class = TextSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Text.objects.filter(type='PPT').order_by('-id')
        username_by = self.request.GET.get('username')
        if username_by:
            queryset = queryset.filter(username=username_by)
        return queryset

# MAIL view GET
class UserMailView(generics.ListAPIView):
    queryset = Text.objects.filter(type='MAIL')
    serializer_class = TextSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Text.objects.filter(type='MAIL').order_by('-id')
        username_by = self.request.GET.get('username')
        if username_by:
            queryset = queryset.filter(username=username_by)
        return queryset

# MAIL view GET
class UserSopView(generics.ListAPIView):
    queryset = Text.objects.filter(type='SOP')
    serializer_class = TextSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Text.objects.filter(type='SOP').order_by('-id')
        username_by = self.request.GET.get('username')
        if username_by:
            queryset = queryset.filter(username=username_by)
        return queryset

# MAIL view GET
class UserResumeView(generics.ListAPIView):
    queryset = Text.objects.filter(type='RESUME')
    serializer_class = TextSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Text.objects.filter(type='RESUME').order_by('-id')
        username_by = self.request.GET.get('username')
        if username_by:
            queryset = queryset.filter(username=username_by)
        return queryset


# Structure
class StructureAPIView(generics.ListCreateAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        queryset = Structure.objects.all().order_by('-id')
        text_id_by = self.request.GET.get('text')
        if text_id_by:
            queryset = queryset.filter(text=text_id_by)
        return queryset

class StructureDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PPTCategoriesAPIView(APIView):
    ## 테스트 할 필요가 있음
    serializer_class = TextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = Text.objects.filter(type='PPT').values_list('category')
        queryset = set(queryset)
        queryset = [category[0] for category in queryset]
        result = {
            '카테고리': queryset
        }
        return Response(result, status=200)
