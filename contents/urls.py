from django.conf.urls import url

from contents.views import WantedContentAPIView, WantedContentDetailsAPIView

urlpatterns = [
    url(r'^job_contents/$', WantedContentAPIView.as_view(), name='job-contents'),
    url(r'^job_contents/(?P<pk>[\w.@+-]+)/$', WantedContentDetailsAPIView.as_view(), name='job-contents-details'),
    ]
