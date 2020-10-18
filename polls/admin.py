from django.contrib import admin
from django.utils import timezone

from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    readonly_fields = ('votes', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'choices_count',)
    search_fields = ('question_text',)
    list_filter = ('pub_date', )
    readonly_fields = ('was_published_recently',)

    fieldsets = (
        ('Dados da questão', {'fields': ('question_text', )}),
        ('Informações', {'fields': ('pub_date', 'was_published_recently', )}),
    )
    inlines = (ChoiceInline,)
    actions = ('action_pub_date_now', )

    def choices_count(self, obj):
        return obj.choice_set.count()

    choices_count.short_description = 'Nº de escolhas'

    def action_pub_date_now(self, request, queryset):
        for question in queryset:
            question.pub_date = timezone.now()
            question.save()
    action_pub_date_now.short_description = 'Publicar agora'
    #fields = ('question_text', 'pub_date', 'maior_choice',)
    #readonly_fields = ('maior_choice',)

admin.site.register(Question, QuestionAdmin)
