from . import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('todo', views.TodoView, basename="todo")

urlpatterns = [
    path('', include(router.urls)),
]
