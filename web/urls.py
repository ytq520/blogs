from django.conf.urls import url
from web import views
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    # 文章
    url(r'^post/', views.post, name='post'),
    # 关于作者
    url(r'^about/', views.about, name='about'),
]