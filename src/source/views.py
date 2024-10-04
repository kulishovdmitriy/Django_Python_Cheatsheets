from django.shortcuts import render # noqa
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from source.models import Information, Source, Topic

# Create your views here.


class TopicListView(ListView):

    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'
    paginate_by = 10


class SourceListView(LoginRequiredMixin, ListView):

    model = Source
    template_name = 'source_list.html'
    context_object_name = 'sources'
    pk_url_kwarg = 'id'
    paginate_by = 10


class InformationDetailView(LoginRequiredMixin, DetailView):
    model = Information
    template_name = 'information_detail.html'
    context_object_name = 'information'
    pk_url_kwarg = 'id'
