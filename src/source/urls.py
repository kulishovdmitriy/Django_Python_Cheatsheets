from django.urls import path

from source.views import InformationDetailView, SourceListView, TopicListView, InformationCreateView, \
    InformationUpdateView, SourceUpdateView

app_name = "source"

urlpatterns = [
    path("topic/", TopicListView.as_view(), name="topic_list"),
    path("source/<int:id>/", SourceListView.as_view(), name="source_list"),
    path("source/update/<int:id>/", SourceUpdateView.as_view(), name="source_update"),
    path('information/create/<int:source_id>/', InformationCreateView.as_view(), name='information_create'),
    path("info/<int:id>/", InformationDetailView.as_view(), name="information_list"),
    path("information/update/<int:id>/", InformationUpdateView.as_view(), name="information_update"),
]
