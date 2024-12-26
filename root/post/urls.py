from django.urls import path
from .views import index
from django.urls import path


urlpatterns = [
    path('', index, name='post'),
]


