from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from source.custom_filters import highlight_code
from source.forms import InformationCreateUpdateForm, SourceCreateForm, TopicCreateForm
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
        context['source'] = self.object.source  # Получаем источник информации
        # Получаем текст из объекта и выделяем код
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
        information.source = source  # Привязываем информацию к источнику
        information.save()
        messages.success(self.request, 'Information created successfully!')
        return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))


class InformationUpdateView(LoginRequiredMixin, UpdateView):
    model = Information
    template_name = 'information_update.html'
    form_class = InformationCreateUpdateForm
    pk_url_kwarg = 'id'  # предполагаем, что в URL передается id информации

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = self.get_object()  # Получаем объект информации
        context['source'] = information.source  # Получаем связанный источник
        return context

    def form_valid(self, form):
        information = form.save(commit=False)
        information.source = information.source  # Здесь вы уже связаны с объектом Source
        information.save()  # Сохраняем объект
        messages.success(self.request, 'Information updated successfully!')
        return HttpResponseRedirect(reverse('source:information_list', kwargs={'id': information.id}))
