from django.db import models 
from django.utils import timezone

from usuario.models import Usuario

class KeyWords(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    date = models.DateTimeField('date published', default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = "KeyWord"
        verbose_name_plural = "KeyWords"