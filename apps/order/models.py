from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    order_sn = models.CharField(unique=True, max_length=100)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)
    consignee = models.CharField(max_length=60, blank=True, null=True)
    province = models.PositiveIntegerField(blank=True, null=True)
    city = models.PositiveIntegerField(blank=True, null=True)
    district = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=60, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    ship_code = models.CharField(max_length=255, blank=True, null=True)
    ship_name = models.CharField(max_length=255, blank=True, null=True)
    shipping_no = models.CharField(max_length=255, blank=True, null=True)
    froms = models.CharField(max_length=10, blank=True, null=True)
    rel_name = models.CharField(max_length=255, blank=True, null=True)
    id_num = models.CharField(max_length=255, blank=True, null=True)
    goods_id = models.CharField(max_length=255, blank=True, null=True)
    goods_sn = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    product_num = models.IntegerField(blank=True, null=True)
    life = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    third_pay_sn = models.CharField(max_length=255, blank=True, null=True)
    third_sn = models.CharField(max_length=255, blank=True, null=True)
    third_tax_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    third_order_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_info'
