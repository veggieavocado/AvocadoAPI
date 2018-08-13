from django.conf.urls import url

from contents.views import (
    WantedContentAPIView,
    WantedContentDetailsAPIView,
    WantedUrlAPIView,
    WantedUrlDetailsAPIView,
    WantedDataAPIView,
    WantedDataDetailsAPIView,
)

urlpatterns = [
    url(r'^job_contents/$', WantedContentAPIView.as_view(), name='job-contents'),
    url(r'^job_contents/(?P<pk>[\w.@+-]+)/$', WantedContentDetailsAPIView.as_view(), name='job-contents-details'),
    url(r'^wanted_url/$', WantedUrlAPIView.as_view(), name='wanted-url'),
    url(r'^wanted_url/(?P<pk>[\w.@+-]+)/$', WantedUrlDetailsAPIView.as_view(), name='wanted-url-details'),
    url(r'^wanted_data/$', WantedDataAPIView.as_view(), name='wanted-url'),
    url(r'^wanted_data/(?P<pk>[\w.@+-]+)/$', WantedDataDetailsAPIView.as_view(), name='wanted-url-details'),
    ]
