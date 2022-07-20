from django.urls import path
from .views import Home, details, Update, Delete

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('details/', details, name="details"),
    path('update/<int:id>/', Update.as_view(), name="update"),
    path('delete/<int:id>/', Delete.as_view(), name="delete"),
]