
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class Menu(models.Model):
    type_choices = ((1, '菜单'), (2, '权限'))
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='菜单名')
    url = models.CharField(max_length=63, null=False, blank=True, verbose_name='url')
    icon = models.CharField(max_length=255, null=True, verbose_name='图标')
    type = models.IntegerField(choices=type_choices, default=1, verbose_name='类型')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children', verbose_name='父菜单')
    desc = models.CharField(max_length=255, null=True, verbose_name='备注')

    class Meta:
        db_table = 'django_menu'


class Role(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name='角色名')
    menus = models.ManyToManyField('Menu', verbose_name='关联菜单')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 'django_role'


class User(AbstractUser):
    username = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name='密码')
    email = models.CharField(max_length=64, null=True, blank=True, verbose_name='邮箱')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
    roles = models.ManyToManyField('Role', related_name='users', verbose_name='角色')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    user_permissions = None
    groups = None
    first_name = None
    last_name = None
    is_staff = None

    class Meta:
        db_table = 'django_user'