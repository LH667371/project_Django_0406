from django_filters.rest_framework import FilterSet

from employee.models import Employee


class EmployeeFilter(FilterSet):
    # from django_filters import filters
    # # 定义范围查询的字段
    # min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    # max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Employee
        fields = ["name"]