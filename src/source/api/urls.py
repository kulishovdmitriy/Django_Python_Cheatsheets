from django.urls import path

from source.api.views_info import InfoListAPIView, InfoCreateAPIView, InfoUpdateDeleteAPIView
from source.api.views_source import SourceListAPIView, SourceCreateAPIView, SourceUpdateDeleteAPIView
from source.api.views_topic import TopicListAPIView, TopicCreateAPIView, TopicUpdateDeleteAPIView


app_name = 'api_source'

urlpatterns = [

    # Topics
    path('topics', TopicListAPIView.as_view(), name='topic_list_api'),
    path('topics/create', TopicCreateAPIView.as_view(), name='topic_create_api'),
    path('topics/<int:pk>', TopicUpdateDeleteAPIView.as_view(), name='topic_update_del_api'),

    # Source
    path('sources', SourceListAPIView.as_view(), name='source_list_api'),
    path('sources/create', SourceCreateAPIView.as_view(), name='source_create_api'),
    path('sources/<int:pk>', SourceUpdateDeleteAPIView.as_view(), name='source_update_del_api'),

    # Info
    path('informations', InfoListAPIView.as_view(), name='info_list_api'),
    path('informations/create', InfoCreateAPIView.as_view(), name='info_create_api'),
    path('informations/<int:pk>', InfoUpdateDeleteAPIView.as_view(), name='info_update_del_api'),
]
