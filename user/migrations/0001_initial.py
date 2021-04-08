# Generated by Django 3.2 on 2021-04-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='账号')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='账号')),
                ('phone', models.CharField(max_length=255, unique=True, verbose_name='手机号')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '其他')], default=2, verbose_name='性别')),
                ('salt', models.CharField(max_length=255, verbose_name='校验')),
            ],
            options={
                'verbose_name': '账户',
                'verbose_name_plural': '账户',
                'db_table': 'user_info',
            },
        ),
    ]
