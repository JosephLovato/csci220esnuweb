from django.urls import path
from gradecalculator.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='MainView'),
]
