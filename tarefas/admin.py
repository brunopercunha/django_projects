from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Projeto, Tarefa

admin.site.register(Projeto)
admin.site.register(Tarefa)
