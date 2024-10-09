from django.urls import path

from source.views import InformationDetailView, SourceListView, TopicListView, InformationCreateView

app_name = "source"

urlpatterns = [
    path("topic/", TopicListView.as_view(), name="topic_list"),
    path("source/<int:id>/", SourceListView.as_view(), name="source_list"),
    path('information/create/<int:source_id>/', InformationCreateView.as_view(), name='information_create'),
    path("info/<int:id>/", InformationDetailView.as_view(), name="information_list"),
]
