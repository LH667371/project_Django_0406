import hashlib

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from user.models import User as UserData
from user.serializers import UserModelSerializer
from utils.response import APIResponse

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your views here.

class User(APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        account = request.data.get('account')
        password = request.data.get('pwd')
        try:
            salt = UserData.objects.get(Q(username=account) | Q(phone=account) | Q(email=account)).salt
        except:
            return APIResponse(401, message="用户名输入错误")
        try:
            password = hashlib.md5(password.encode() + salt.encode())
            user = UserData.objects.get(
                Q(username=account, password=password.hexdigest()) | Q(phone=account, password=password.hexdigest()))
            if user:
                # 通过用户生成载荷  根据载荷签发token
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return APIResponse(200, message="登录成功", name=user.name, token=token)
        except Exception as e:
            print(e)
            return APIResponse(402, message="密码输入错误")

class UserRegister(APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        request_data = request.data
        try:
            serializer = UserModelSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            admin_obj = serializer.save()
            if admin_obj:
                return APIResponse(200, True)
        except Exception as e:
            print(e)
            return APIResponse(400, message="您提交的注册信息有误")
