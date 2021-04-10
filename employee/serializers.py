from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from employee.models import Employee, Department


class EmpModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'age', 'gender', 'birthday', 'head_pic', 'depart', 'depart_name', 'sex']
        extra_kwargs = {
            'depart_name': {
                'read_only': True,
            },
            'sex': {
                'read_only': True,
            },
        }
    def validate(self, attrs):
        try:
            if not self.initial_data['id']:
                attrs['id'] = Employee.objects.values('id').last()['id'] + 1
            else:
                attrs['id'] = self.initial_data['id']
        except:
            attrs['id'] = 1000
        return attrs

class DepartModelSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
