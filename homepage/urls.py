# Note!!! this doc is high key useless at the moment.

from django.urls import path
from homepage.views import index

urlpatterns = [
    path('/', index)
]