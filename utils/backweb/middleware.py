from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from backweb.models import MyUser

# 中间件实现登录


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 在访问登录和注册的时候，不需要做以下的登录校验功能

        if request.path in ['/backweb/login/', '/backweb/register/', '/web/index/']:
            return None

        # 登录校验
        user_id = request.session.get('user_id')
        if user_id:
            user = MyUser.objects.get(pk=user_id)
            request.user = user

        else:
            return HttpResponseRedirect('/backweb/login/')
