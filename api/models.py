from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Project(models.Model):
    # user
    user = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)
    # title project
    title = models.CharField(max_length=50)
    # description project
    description = models.TextField()
    # technology to use
    technology = models.CharField(max_length=50)
    # date created
    created_at = models.DateTimeField(auto_now_add=True)
    