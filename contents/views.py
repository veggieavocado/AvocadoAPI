from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from contents.models import WantedContent, WantedUrl, WantedData
from contents.serializers import (
    WantedContentSerializer,
    WantedUrlSerializer,
    WantedDataSerializer,
)

from utils.paginations import StandardResultPagination

# WantedContent view GET POST
class WantedContentAPIView(generics.ListCreateAPIView):
    queryset = WantedContent.objects.all()
    serializer_class = WantedContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = WantedContent.objects.all().order_by('id')
        title_by = self.request.GET.get('title')
        company_by = self.request.GET.get('company')
        loaction_by = self.request.GET.get('location')

        if title_by:
            queryset = queryset.filter(title=title_by)
        if company_by:
            queryset = queryset.filter(company=company_by)
        if loaction_by:
            queryset = queryset.filter(location=loaction_by)
        return queryset

# WantedContent view PUT DELETE
class WantedContentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WantedContent.objects.all()
    serializer_class = WantedContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# WantedUrl view GET POST
class WantedUrlAPIView(generics.ListCreateAPIView):
    queryset = WantedUrl.objects.all().order_by('id')
    serializer_class = WantedUrlSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

# Wantedurl view PUT DELETE
class WantedUrlDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WantedUrl.objects.all()
    serializer_class = WantedUrlSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# WantedUrl view GET POST
class WantedDataAPIView(generics.ListCreateAPIView):
    queryset = WantedData.objects.all().order_by('id')
    serializer_class = WantedDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

# Wantedurl view PUT DELETE
class WantedDataDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WantedData.objects.all()
    serializer_class = WantedDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
