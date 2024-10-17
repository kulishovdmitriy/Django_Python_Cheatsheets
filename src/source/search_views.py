from django.shortcuts import render

from source.models import Topic, Source, Information


def search_topics(request):
    query = request.GET.get('q')
    if query:
        topics = Topic.objects.filter(name__icontains=query)
    else:
        topics = Topic.objects.all()

    return render(request, 'topic_list.html', {'topics': topics})


def search_source(request):
    query = request.GET.get('q')
    if query:
        sources = Source.objects.filter(title__icontains=query)
    else:
        sources = Source.objects.all()

    # Добавляем информацию для каждого источника
    for source in sources:
        source.information_list = Information.objects.filter(source=source)

    return render(request, 'source_list.html', {'sources': sources})
