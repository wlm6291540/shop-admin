from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    order_status_choice = ((-5, "拒绝退换货"), (-4, "申请换货"), (-3, "已申请退换货"), (-2, "同意换货"), (-1, "退款"), (0, "创建"),
                    (1, "已支付"), (3, "配货中"), (4, "未发货"), (5, "已发货"), (6, "已收货"), (7, "已完成"), (8, "已取消"),
                    (9, "订单已生效"), (10, "拆单完成"), (11, "海关审核中"))
    order_sn = models.CharField(unique=True, max_length=100)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.IntegerField(choices=order_status_choice, blank=True, null=True)
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
