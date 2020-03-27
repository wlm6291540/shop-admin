from django.db import models


# Create your models here.


class Users(models.Model):
    auth_status_choices = ((0, '未认证或认证失败'), (1, '认证通过'))
    user_id = models.CharField(primary_key=True, max_length=100)
    user_name = models.CharField(unique=True, max_length=60, verbose_name='用户名')
    company_name = models.CharField(max_length=60)
    password = models.CharField(max_length=32)
    user_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='用户现有金额')
    frozen_money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='用户冻结金额')
    reg_time = models.PositiveIntegerField(verbose_name='注册时间')
    auth_status = models.PositiveIntegerField(choices=auth_status_choices, verbose_name='认证状态')
    private_key = models.TextField()
    public_key = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
