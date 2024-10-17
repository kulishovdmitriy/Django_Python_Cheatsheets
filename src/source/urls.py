from django.urls import path

from source.views import InformationDetailView, SourceListView, TopicListView, InformationCreateView, \
    InformationUpdateView, SourceUpdateView
from source.search_views import search_topics, search_source


app_name = "source"

urlpatterns = [

    # Topic
    path("topic/", TopicListView.as_view(), name="topic_list"),
    path('search/topic/', search_topics, name='search_topic'),

    # Source
    path("source/<int:id>/", SourceListView.as_view(), name="source_list"),
    path("source/update/<int:id>/", SourceUpdateView.as_view(), name="source_update"),
    path('search/source/', search_source, name='search_source'),

    # Info
    path('information/create/<int:source_id>/', InformationCreateView.as_view(), name='information_create'),
    path("information/<int:id>/", InformationDetailView.as_view(), name="information_list"),
    path("information/update/<int:id>/", InformationUpdateView.as_view(), name="information_update"),
]
