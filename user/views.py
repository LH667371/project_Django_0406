import hashlib
import random
import string

from captcha.image import ImageCaptcha
from django.db.models import Q
from django.http import HttpResponse
from rest_framework.views import APIView

from user.models import User as UserData
from user.serializers import UserModelSerializer
from utils.response import APIResponse


# Create your views here.

class User(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            salt = UserData.objects.get(Q(email=username) | Q(phone=username)).salt
        except:
            return APIResponse(401, message="用户名输入错误")
        try:
            password = hashlib.md5(password.encode() + salt.encode())
            user = UserData.objects.get(
                Q(email=username, password=password.hexdigest()) | Q(phone=username, password=password.hexdigest()))
            if user:
                return APIResponse(200, message="登录成功", name=user.name)
        except:
            return APIResponse(402, message="密码输入错误")

    def post(self, request, *args, **kwargs):
        request_data = request.data
        try:
            serializer = UserModelSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            admin_obj = serializer.save()
            name = UserData.objects.filter(Q(email=UserModelSerializer(admin_obj).data['email']) | Q(
                phone=UserModelSerializer(admin_obj).data['phone'])).values('name')
            if admin_obj:
                return APIResponse(200, True, results=name)
        except Exception as e:
            print(e)
            return APIResponse(400, message="您提交的注册信息有误")


class Captcha(APIView):
    # 验证码视图
    def get(self, request, *args, **kwargs):
        # 声明一个图片验证码对象
        image = ImageCaptcha()
        # 生成随机的4位验证码
        code = random.sample(string.ascii_letters + string.digits, 4)
        code = ''.join(code)
        print(code)
        print(request.session.session_key)
        request.session['code'] = code.lower()
        # 将验证码写入图片中
        data = image.generate(code)
        return HttpResponse(data, 'image/png')

    def post(self, request, *args, **kwargs):
        print(request.session.session_key)
        print(request.session.get('code'))
        return APIResponse('ok')
