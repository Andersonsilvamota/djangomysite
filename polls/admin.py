from django.contrib import admin

from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text', 'pub_date', 'maior_choice',)
    readonly_fields = ('maior_choice',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)