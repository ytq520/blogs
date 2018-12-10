from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render

from backweb.models import ArticleType, Article


def index(request):
    if request.method == 'GET':
        # 查文章
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 将所有的数据按照每一页5条数据进行切块处理
        paginator = Paginator(articles, 10)
        # 获取页面的第几条数据
        pages = paginator.page(page)

        # 查文章类型和数量
        types = ArticleType.objects.all()
        t = types.order_by('id').values('id')
        lists = []
        for i in t:
            art = Article.objects.filter(tf=i['id']).aggregate(Count('tf'))

            lists += art.values()
            continue
        dict = {}
        for num in range(len(types)):
            dict[types[num]] = lists[num]
        return render(request, 'web/index.html', {'dict': dict, 'pages': pages})


def post(request):
    if request.method == 'GET':
        # 查文章
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 将所有的数据按照每一页5条数据进行切块处理
        paginator = Paginator(articles, 10)
        # 获取页面的第几条数据
        pages = paginator.page(page)

        # 查文章类型和数量
        types = ArticleType.objects.all()
        t = types.order_by('id').values('id')
        lists = []
        for i in t:
            art = Article.objects.filter(tf=i['id']).aggregate(Count('tf'))

            lists += art.values()
            continue
        dict = {}
        for num in range(len(types)):
            dict[types[num]] = lists[num]
        return render(request, 'web/list.html', {'dict': dict, 'pages': pages})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')