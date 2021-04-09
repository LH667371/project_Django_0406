import hashlib
import random
import string

from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('email', 'password', 'salt')

        extra_kwargs = {
            'username': {
                'min_length': 4,
                'error_messages': {
                    'min_length': '长度太短了'
                }
            },
            'email': {
                'min_length': 4,
                'error_messages': {
                    'min_length': '长度太短了'
                }
            },
            'phone': {
                'min_length': 11,
                'max_length': 11,
                'error_messages': {
                    'min_length': '长度太短了'
                }
            },
            'password': {
                'required': True,
                'write_only': True,
                'error_messages': {
                    'required': '密码必填',
                }
            },
            'name': {
                'write_only': True,
            },
            'gender': {
                'write_only': True,
            },
            'salt': {
                'required': False,
                'write_only': True,
            },
        }

    # 用户名重复
    def validate_email(self, email):
        user = User.objects.filter(email=email).first()
        if user:
            raise exceptions.ValidationError("邮箱已存在")
        return email

    def validate_phone(self, phone):
        user = User.objects.filter(phone=phone).first()
        if user:
            raise exceptions.ValidationError("手机号已存在")
        return phone

    def validate(self, attrs):
        try:
            attrs['id'] = User.objects.values('id').last()['id'] + 1
        except:
            attrs['id'] = 1
        attrs['salt'] = ''.join(
            random.sample(string.ascii_letters + string.digits + string.punctuation, random.randint(5, 10)))
        attrs['password'] = (hashlib.md5(attrs['password'].encode() + attrs['salt'].encode())).hexdigest()
        return attrs
