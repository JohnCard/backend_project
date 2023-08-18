from django.contrib import admin
from .models import Project
from .serializers import Programmer

# Register your models here.
admin.site.register(Project)