from django.urls import path

from source.views import InformationDetailView, SourceListView, TopicListView

app_name = "source"

urlpatterns = [
    path("topic/", TopicListView.as_view(), name="topic_list"),
    path("source/<int:id>/", SourceListView.as_view(), name="source_detail"),
    path("info/<int:id>/", InformationDetailView.as_view(), name="information_detail"),
]
