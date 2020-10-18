from datetime import timedelta
from django.db import models
from django.utils import timezone

class Question(models.Model):
    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ('pub_date',)

    question_text = models.CharField('Texto da questão', max_length=200, help_text='Informe o texto da questão.')
    pub_date = models.DateTimeField('Data de publicação', default=timezone.now)
    is_public = models.BooleanField('Publicados', default=True)

    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem

    was_published_recently.short_description = "Publicado recentimente"
    was_published_recently.boolean = True

    def __str__(self):
        return self.question_text

    @property
    def maior_choice(self):
        maior = self.choice_set.aggregate(models.Max('votes'))['votes__max']
        return self.choice_set.get(votes__exact=maior)

class Choice(models.Model):
    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Questâo')
    choice_text = models.CharField('Texto do choice', max_length=200)
    pub_date = models.DateTimeField('Data de publicacao', default=timezone.now)
    votes = models.IntegerField('Nºde Votos', default=0)

    def was_published_recently_Choice(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem

    def __str__(self):
        return self.choice_text