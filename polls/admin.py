from django.contrib import admin
from django.utils import timezone

from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    readonly_fields = ('votes', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'choices_count', 'is_public', )
    search_fields = ('question_text',)
    list_filter = ('pub_date', )
    readonly_fields = ('was_published_recently', 'maior_choice', 'is_public', )

    fieldsets = (
        ('Dados da questão', {'fields': ('question_text', )}),
        ('Informações', {'fields': ('pub_date', 'was_published_recently', 'is_public', )}),
    )
    inlines = (ChoiceInline,)
    actions = ('action_pub_date_now', 'public_question', 'unpublish', )

    def choices_count(self, obj):
        return obj.choice_set.count()
    choices_count.short_description = 'Nº de escolhas'

    def pub_date_now(self, request, queryset):
        for question in queryset:
            question.pub_date = timezone.now()
            question.save()
    pub_date_now.short_description = 'Publicar agora'
    #fields = ('question_text', 'pub_date', 'maior_choice',)
    #readonly_fields = ('maior_choice',)

    def public_question(self, request, queryset):
        for question in queryset:
            question.is_public = True
            question.save()

    public_question.short_description = 'Publicar questão'

    def unpublish(self, request, queryset):
        for question in queryset:
            question.is_public = False
            question.save()

    unpublish.short_description = 'Despublicar questão'


admin.site.register(Question, QuestionAdmin)
