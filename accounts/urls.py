from django.conf.urls import url
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
    )

from accounts.views import (
    UserAPIView,
    UserDetailsAPIView,
    UserLoginAPIView,
    ProfileAPIView,
    ProfileDetailsAPIView,
)

urlpatterns = [
    # token maker
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # basic user login, info urls
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^user/$', UserAPIView.as_view(), name="user"),
    url(r'^user/(?P<username>[\w.@+-]+)/$', UserDetailsAPIView.as_view(), name="user-details"),

    # user profile related urls
    url(r'^profile/$', ProfileAPIView.as_view(), name="profile"),
    url(r'^profile/(?P<pk>[\w.@+-]+)/$', ProfileDetailsAPIView.as_view(), name="profile-details"),
]
