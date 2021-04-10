from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from employee.jwt_authentication import JWTAuthentication
from employee.models import Employee, Department
from employee.pagination import MyPageNumberPagination
from employee.serializers import EmpModelSerializer, DepartModelSerializer
from utils.response import APIResponse


# Create your views here.


class EmpAPIView(GenericAPIView,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 CreateModelMixin,
                 UpdateModelMixin,
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class SerchEmpAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    # 指定当前视图要使用的过滤器类
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    # 指定当前视图的搜索条件  通过哪个字段进行搜索
    search_fields = ['id', 'name', 'salary', 'depart__department', 'age']
    # 指定排序的字段
    ordering = ['id']
    # filter_class = EmployeeFilter
    pagination_class = MyPageNumberPagination
