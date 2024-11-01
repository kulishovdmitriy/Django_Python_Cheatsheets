from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from source.custom_filters import highlight_code
from source.forms import InformationCreateUpdateForm, SourceCreateUpdateForm, TopicCreateForm
from source.models import Information, Source, Topic

# Create your views here.


class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            context['form'] = TopicCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TopicCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Topic created successfully!')
                return HttpResponseRedirect(reverse('source:topic_list'))
        return self.get(request, *args, **kwargs)


class SourceListView(LoginRequiredMixin, ListView):
    model = Source
    template_name = 'source_list.html'
    context_object_name = 'sources'
    pk_url_kwarg = 'id'
    paginate_by = 12

    def get_queryset(self):
        topic_id = self.kwargs.get('id')
        return Source.objects.filter(topic_id=topic_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        topic = Topic.objects.get(pk=self.kwargs.get('id'))
        context['topic'] = topic

        for source in context['sources']:
            source.information_list = Information.objects.filter(source=source)

        if self.request.user.is_authenticated and self.request.user.is_superuser:
            context['form'] = SourceCreateUpdateForm()
        return context

    def post(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk=self.kwargs.get('id'))  # Получаем текущий топик
        form = SourceCreateUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            source = form.save(commit=False)
            source.topic = topic
            source.save()
            messages.success(request, 'Source created successfully!')
            return HttpResponseRedirect(reverse('source:source_list', kwargs={'id': topic.id}))
        return self.get(request, *args, **kwargs)


class SourceUpdateView(LoginRequiredMixin, UpdateView):
    model = Source
    template_name = 'source_update.html'
    context_object_name = 'source'
    form_class = SourceCreateUpdateForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        source = form.save(commit=False)
        source.save()

        messages.success(self.request, 'Source updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('source:source_list', kwargs={'id': self.object.topic.id})


class InformationDetailView(LoginRequiredMixin, DetailView):
    model = Information
    template_name = 'information_list.html'
    context_object_name = 'information'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object.source
        text_with_highlighting = highlight_code(self.object.text)

        context['info_text'] = text_with_highlighting
        return context


class InformationCreateView(LoginRequiredMixin, CreateView):
    model = Information
    template_name = 'information_list.html'
    form_class = InformationCreateUpdateForm

    def form_valid(self, form):
        source_id = self.kwargs.get('source_id')
        source = get_object_or_404(Source, pk=source_id)
        information = form.save(commit=False)
        information.source = source
        information.save()
        messages.success(self.request, 'Information created successfully!')
        return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))


class InformationUpdateView(LoginRequiredMixin, UpdateView):
    model = Information
    template_name = 'information_update.html'
    form_class = InformationCreateUpdateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = self.get_object()
        context['source'] = information.source
        return context

    def form_valid(self, form):
        information = form.save(commit=False)
        information.source = information.source
        information.save()
        messages.success(self.request, 'Information updated successfully!')
        return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))
