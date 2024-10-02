from django.contrib import admin

from source.models import Topic, Source, Information

# Register your models here.


# Представление модели Information в панели Source
class InformationInline(admin.TabularInline):
    model = Information
    fields = ('text',)
    show_change_link = True
    extra = 0


# Позволяет показать/редактировать модель Information в меню Source
class SourceAdmin(admin.ModelAdmin):
    inlines = (InformationInline,)


# Представление модели Source в панели Topic
class SourceInline(admin.TabularInline):
    model = Source
    fields = ('title', 'description', 'image')
    show_change_link = True
    extra = 0
    ordering = ('title',)


# Позволяет показать/редактировать модель Source в меню Topic
class TopicAdmin(admin.ModelAdmin):
    inlines = (SourceInline,)


# Подключение наших моделей в админ панель
admin.site.register(Topic, TopicAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Information)
