from django.urls import path
from django.views.generic import TemplateView, RedirectView

from .views import test_view, test_sec,detail_obj, tests

urlpatterns = [
    path('test_view/',test_view),
    path('test_sec/',test_sec),
    path('detail_obj/',detail_obj),
    path('testings/',tests)
]