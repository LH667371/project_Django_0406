from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from employee.jwt_authentication import JWTAuthentication
from employee.models import Employee, Department
from employee.serializers import EmpModelSerializer, DepartModelSerializer
# Create your views here.
from utils.response import APIResponse


class EmpAPIView(GenericAPIView,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 CreateModelMixin,
                 UpdateModelMixin
                 ):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    # 登录用户才可以访问
    permission_classes = [IsAuthenticated]
    # 解析访问此视图请求中携带的 jwt token
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # print(request.data)
        # return APIResponse(200, 'ok')

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(200, message="删除成功")

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # print(request.data)
        self.partial_update(request, *args, **kwargs)
        return APIResponse(200, message="修改成功")


class DepartAPIView(GenericAPIView,
                    ListModelMixin,
                    RetrieveModelMixin,
                    ):
    queryset = Department.objects.all()
    serializer_class = DepartModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
