from django.urls import path
from . import views

urlpatterns = [
    path('sayhi/', views.say_hi),
    path('sayhi/<str:student>', views.say_hi_student)
]