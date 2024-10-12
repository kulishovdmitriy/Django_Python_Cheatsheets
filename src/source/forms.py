from django.forms import ModelForm

from source.models import Topic, Source, Information


class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'image']


class SourceCreateForm(ModelForm):
    class Meta:
        model = Source
        fields = ['title', 'description', 'image']


class InformationCreateUpdateForm(ModelForm):
    class Meta:
        model = Information
        fields = ['text']
