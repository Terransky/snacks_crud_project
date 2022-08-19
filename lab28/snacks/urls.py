from django.urls import path
from .views import HomePageView  # the class from .views.py, don't know why it needs dot notation though

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
