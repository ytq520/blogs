
from django.conf.urls import url
from backweb import views

urlpatterns = [

    # 注册
    url(r'^register/', views.register),
    # 登陆
    url(r'^login/', views.login, name='login'),
    # 主页
    url(r'^index/', views.index, name='index'),
    # 创建文章
    url(r'^add/', views.add, name='add'),
    # 退出登录
    url(r'^logout/', views.logout, name='logout'),
    # 删除文章
    url(r'^del_art/(\d+)/', views.del_art, name='del_art'),
    # 编辑文章
    url(r'^edit_art/(\d+)/', views.edit_art, name='edit_art'),
    # 推荐书籍
    url(r'^recommend/', views.recommend, name='recommend'),
    # 文章类型
    url(r'^review/', views.review, name='review'),
    # 用户
    url(r'^user/', views.user, name='user'),
    # 删除用户
    url(r'^del_user/(\d+)/', views.del_user, name='del_user'),

]