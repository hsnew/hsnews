from django.urls import path
from one_app.views import ListNews

urlpatterns = [
    path('', ListNews.as_view())
]