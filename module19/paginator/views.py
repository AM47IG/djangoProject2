from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *


# Create your views here.
def paginator(request):
    posts = Post.objects.all().order_by('-created_at')
    el_on_page = request.GET.get('el_on_page', 3)
    paginator = Paginator(posts, per_page=el_on_page, orphans=2)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'el_on_page': el_on_page
    }
    return render(request, 'paginator/paginator.html', context)
