from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from source.forms import InformationCreateForm, SourceCreateForm, TopicCreateForm
from source.models import Information, Source, Topic

# Create your views here.


class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем форму в контекст
        if self.request.user.is_authenticated and self.request.user.is_active:
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
    pk_url_kwarg = 'id'  # Получение ID топика из URL
    paginate_by = 10

    def get_queryset(self):
        # Получаем ID топика из URL
        topic_id = self.kwargs.get('id')
        # Возвращаем только те источники, которые принадлежат текущему топику
        return Source.objects.filter(topic_id=topic_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем текущий топик
        topic = Topic.objects.get(pk=self.kwargs.get('id'))
        context['topic'] = topic  # Добавляем топик в контекст

        # Добавляем информацию, связанную с источником, в контекст
        for source in context['sources']:
            source.information_list = Information.objects.filter(source=source)  # Получаем информацию, связанную с источником

        # Добавляем форму в контекст, если пользователь аутентифицирован
        if self.request.user.is_authenticated and self.request.user.is_active:
            context['form'] = SourceCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk=self.kwargs.get('id'))  # Получаем текущий топик
        form = SourceCreateForm(request.POST, request.FILES)
        if form.is_valid():
            source = form.save(commit=False)
            source.topic = topic  # Связываем новый источник с топиком
            source.save()
            messages.success(request, 'Source created successfully!')
            return HttpResponseRedirect(reverse('source:source_list', kwargs={'id': topic.id}))  # Перенаправляем обратно на список
        return self.get(request, *args, **kwargs)


class InformationDetailView(LoginRequiredMixin, DetailView):
    model = Information
    template_name = 'information_list.html'
    context_object_name = 'information'
    pk_url_kwarg = 'id'  # Этот id должен быть идентификатором информации

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_active:
            context['form'] = InformationCreateForm()
            # Добавляем источник в контекст для использования в форме
            context['source'] = self.object.source
        return context

    def post(self, request, *args, **kwargs):
        source_id = self.kwargs.get('id')  # Получаем ID источника из URL
        source = Source.objects.get(pk=source_id)  # Получаем источник
        form = InformationCreateForm(request.POST, request.FILES)
        if form.is_valid():
            information = form.save(commit=False)
            information.source = source  # Связываем новую информацию с источником
            information.save()
            messages.success(request, 'Info created successfully!')
            return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))  # Перенаправляем на детали новой информации
        return self.get(request, *args, **kwargs)


class InformationCreateView(LoginRequiredMixin, CreateView):
    model = Information
    template_name = 'information_list.html'
    form_class = InformationCreateForm

    def form_valid(self, form):
        source_id = self.kwargs.get('source_id')
        source = get_object_or_404(Source, pk=source_id)
        information = form.save(commit=False)
        information.source = source  # Привязываем информацию к источнику
        information.save()
        messages.success(self.request, 'Information created successfully!')
        return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))
