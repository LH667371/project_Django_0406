from django.db import models


# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "其他"),
    )
    email = models.CharField(max_length=255, unique=True, verbose_name='邮箱')
    phone = models.CharField(max_length=255, unique=True, verbose_name='手机号')
    password = models.CharField(max_length=255, verbose_name='密码')
    name = models.CharField(max_length=255, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=gender_choices, default=2, verbose_name='性别')
    salt = models.CharField(max_length=255, verbose_name='校验')

    class Meta:
        db_table = 'user_info'
        verbose_name = '账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
