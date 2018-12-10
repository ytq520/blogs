from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.Artform import AddArtForm, EditArtForm
from backweb.models import MyUser, ArticleType, Article


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    # 注册验证
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

    # 1.判断用户存不存在，用户是否已经被注册
    user = MyUser.objects.filter(username=username).first()
    if username:
        if user:
            err_name = '该用户名已经存在，请重新输入'
            return render(request, 'backweb/register.html', {'err_name': err_name})
    else:
        err_name = '用户名不能为空'
        return render(request, 'backweb/register.html', {'err_name': err_name})
    # 2.判断密码和确认密码是否一致
    if password and password2:
        if not password == password2:
            err_pwd = '密码和确认密码不一致'
            return render(request, 'backweb/register.html', {'err_pwd': err_pwd})
    elif not password:
        err_pwd = '密码不能为空'
        return render(request, 'backweb/register.html', {'err_pwd': err_pwd})
    elif not password2:
        err_pwd = '确认密码不能为空'
        return render(request, 'backweb/register.html', {'err_pwd': err_pwd})
    # 3、用户名不存在且不为空，密码与确认密码相同时，保存在user表中
    MyUser.objects.create(username=username, password=password)
    return HttpResponseRedirect('/backweb/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    if request.method == 'POST':
        # 获取用户名
        username = request.POST.get('username')
        password = request.POST.get('password')

    # 1.查询数据库中的用户名和密码对应的用户对象
    user = MyUser.objects.filter(username=username, password=password).first()
    if not user:
        err_user = '用户名/密码错误'
        return render(request, 'backweb/login.html', {'err_user': err_user})

    # 使用session实现登录操作
    request.session['user_id'] = user.id

    # 跳转到首页
    return HttpResponseRedirect('/backweb/index/')





def add(request):
    if request.method == 'GET':
        return render(request, 'backweb/add.html')
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            tf = request.POST.get('tf')
            tf_id = ArticleType.objects.filter(pk=tf).first()
            if tf_id:
                Article.objects.create(title=title, author=author, desc=desc, content=content, tf=tf_id)
                return HttpResponseRedirect('/backweb/index/')
            else:
                err_name = '没有此类型'
                return render(request, 'backweb/add.html', {'err_name': err_name})
        else:
            return render(request, 'backweb/add.html', {'form': form})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/backweb/logout/')


def del_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/backweb/index/')


def edit_art(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add.html', {'article': article})
    if request.method == 'POST':
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            # 验证成功
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            tf = request.POST.get('f')
            article = Article.objects.filter(pk=id).first()
            tf_id = ArticleType.objects.filter(pk=tf).first()
            if tf_id:
                article.title = title
                article.author = author
                article.desc = desc
                article.content = content
                article.f = tf_id
                article.save()
                return HttpResponseRedirect('/backweb/index/')
            else:
                err_name = '没有此类型'
                return render(request, 'backweb/add.html', {'err_name': err_name})
        else:
            # 验证失败
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add.html',
                          {'form': form, 'article': article})


def index(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 将所有的数据按照每一页5条数据进行切块处理
        paginator = Paginator(articles, 10)
        # 获取页面的第几条数据
        pages = paginator.page(page)
        articles = Article.objects.all()
        return render(request, 'backweb/index.html', {'pages': pages, 'articles': articles})


def recommend(request):
    if request.method == 'GET':
        return render(request, 'backweb/recommend.html')


def review(request):
    if request.method == 'GET':
        types = ArticleType.objects.all().order_by('id')
        t = types.values('id')
        lists = []
        for i in t:
            art = Article.objects.filter(tf=i['id']).aggregate(Count('tf'))

            lists += art.values()
            continue
        dict = {}
        for num in range(len(types)):
            dict[types[num]] = lists[num]

        return render(request, 'backweb/atype.html', {'dict': dict})


def user(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        users = MyUser.objects.all()
        # 将所有的数据按照每一页5条数据进行切块处理
        paginator = Paginator(users, 5)
        # 获取页面的第几条数据
        pages = paginator.page(page)

        return render(request, 'backweb/user.html', {'pages': pages, 'users': users})


def del_user(request, id):
    if request.method == 'GET':
        MyUser.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/backweb/user/')


