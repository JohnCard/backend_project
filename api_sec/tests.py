from django.test import TestCase
from datetime import datetime
from .models import Project
import json
# Create your tests here.
print(datetime.now().strftime('%a, %d %b %Y %H:%M'))
for i in Project.objects.all():
    print(json.load(i))