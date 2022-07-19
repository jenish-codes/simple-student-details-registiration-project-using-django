from django.urls import path
from .views import Home, details, Update, delete

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('details/', details, name="details"),
    path('update/<int:id>/', Update.as_view(), name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]