
from django.urls import path
from .views import CartView

urlpatterns = [
    path('api/<int:userid>/', CartView.as_view()),
]