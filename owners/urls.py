from django.urls import path
from owners.views import OwnersView
from owners.views import DogsView

urlpatterns = [
    path('', OwnersView.as_view()),
    path('/dog', DogsView.as_view()),
]
