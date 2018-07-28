from django.conf.urls import url

from services.views import (
    SentenceAPIView,
    SentenceDetailsAPIView,
    TextAPIView,
    TextDetailsAPIView,
    WordAPIView,
    WordDetailsAPIView,
    StateAPIView,
    StateDetailsAPIView,
    UserPptView,
    StructureAPIView,
    StructureDetailAPIView,

    PPTCategoriesAPIView,
    EmailCategoriesAPIView,
    TextFreqAPIView,
)

urlpatterns = [
    url(r'^sentence/$', SentenceAPIView.as_view(), name='sentences'),
    url(r'^sentence/(?P<pk>[\w.@+-]+)/$', SentenceDetailsAPIView.as_view(), name='sentence-details'),
    url(r'^text/$', TextAPIView.as_view(), name='texts'),
    url(r'^text/(?P<pk>[\w.@+-]+)/$', TextDetailsAPIView.as_view(), name='text-details'),
    url(r'^word/$', WordAPIView.as_view(), name='words'),
    url(r'^word/(?P<pk>[\w.@+-]+)/$', WordDetailsAPIView.as_view(), name='word-detail'),
    url(r'^state/$', StateAPIView.as_view(), name='states'),
    url(r'^state/(?P<pk>[\w.@+-]+)/$', StateDetailsAPIView.as_view(), name='state-details'),

    # User 템플릿 리스트 API
    url(r'^ppt/$', UserPptView.as_view(), name='user-ppt'),

    # Structure API
    url(r'^sent_swap/$', StructureAPIView.as_view(), name='sent-swap'),
    url(r'^sent_swap/(?P<pk>[\w.@+-]+)/$', StructureDetailAPIView.as_view(), name='sent-swap-detail'),

    # 프론트앤드 용도 API
    url(r'^ppt_categories/$', PPTCategoriesAPIView.as_view(), name='ppt-categories'),
    url(r'^mail_categories/$', EmailCategoriesAPIView.as_view(), name='mail-categories'),
    # 텍스트 분석 API
    url(r'^text_analysis/freq/$', TextFreqAPIView.as_view(), name='nltk_freq'),
]
