from rest_framework.serializers import ModelSerializer

from employee.models import Employee


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
            'id': {
                'read_only': True,
            }
        }
