from django.conf.urls import url
from django.urls import path, include
from .views import (
    TestListApiView,TestDetailApiView
)

urlpatterns = [
    path('api', TestListApiView.as_view()),
    path('api/<int:id>',TestDetailApiView.as_view()),
]