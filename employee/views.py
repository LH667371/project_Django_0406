from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, \
    UpdateModelMixin

from employee.models import Employee
from employee.serializers import EmpModelSerializer
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
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(200, message="删除成功")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return APIResponse(200, message="修改成功")
