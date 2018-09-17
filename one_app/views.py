# создать вью полной новоти, шаблон для этой новости, переход на нее.
from django.shortcuts import render
from django.views.generic import View

from one_app.models import News


class ListNews(View):
    """Список новостей"""
    def get(self, request):
        news = News.objects.all()
        return render(request, "one_app/list.html", {"news": news})

