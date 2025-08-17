from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="tarefas")
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
