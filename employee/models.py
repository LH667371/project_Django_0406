from django.db import models


# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=255, unique=True, verbose_name='部门')

    class Meta:
        db_table = 'depart_info'
        verbose_name = '部门表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.department


class Employee(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "其他"),
    )
    name = models.CharField(max_length=255, verbose_name='姓名')
    salary = models.FloatField(verbose_name='工资')
    age = models.CharField(max_length=255, verbose_name='年龄')
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')
    birthday = models.DateField(verbose_name='生日')
    head_pic = models.ImageField(upload_to='pic', null=True, verbose_name='头像')
    depart = models.ForeignKey(to=Department, on_delete=models.CASCADE, verbose_name='部门')

    @property
    def depart_name(self):
        return self.depart.department

    @property
    def sex(self):
        return self.get_gender_display()

    class Meta:
        db_table = 'employee_info'
        verbose_name = '员工信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
