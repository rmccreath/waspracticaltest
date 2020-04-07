from django.shortcuts import get_object_or_404, render

from .models import NewsStory


def index(request):
    latest_newsstory_list = NewsStory.objects.order_by('-pub_date')[:5]
    context = {
        'latest_newsstory_list': latest_newsstory_list,
    }
    return render(request, 'wasnews/index.html', context)


def news(request, newsstory_id):
    newsstory = get_object_or_404(NewsStory, pk=newsstory_id)
    return render(request, 'wasnews/news.html', {'newsstory': newsstory})
