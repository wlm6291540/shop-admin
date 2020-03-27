# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    cat_id = models.CharField(max_length=100)
    goods_sn = models.CharField(max_length=60)
    bar_code = models.CharField(max_length=255)
    goods_name = models.CharField(max_length=120)
    brand_id = models.PositiveIntegerField()
    goods_number = models.PositiveIntegerField()
    is_freepost = models.PositiveIntegerField(blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    warn_number = models.IntegerField(blank=True, null=True)
    goods_desc = models.TextField(blank=True, null=True)
    desc_mobile = models.TextField(blank=True, null=True)
    goods_thumb = models.CharField(max_length=255)
    is_on_sale = models.IntegerField()
    is_delete = models.IntegerField()
    status = models.IntegerField()
    pinyin_keyword = models.TextField(blank=True, null=True)
    goods_unit = models.CharField(max_length=15, blank=True, null=True)
    pattern = models.IntegerField(blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    source_code = models.CharField(max_length=255, blank=True, null=True)
    lifes = models.CharField(max_length=255, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    spec = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255)
    brand_letter = models.CharField(max_length=255, blank=True, null=True)
    brand_first_char = models.CharField(max_length=1, blank=True, null=True)
    brand_logo = models.CharField(max_length=255, blank=True, null=True)
    index_img = models.CharField(max_length=255, blank=True, null=True)
    brand_bg = models.CharField(max_length=255, blank=True, null=True)
    brand_desc = models.TextField(blank=True, null=True)
    site_url = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True, default=1)
    is_delete = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    name_pinyin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_brand'


class GoodsCategory(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=100)
    cat_name = models.CharField(max_length=90)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    cat_desc = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.PositiveIntegerField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    style_icon = models.CharField(max_length=50, blank=True, null=True)
    cat_icon = models.CharField(max_length=255, blank=True, null=True)
    pinyin_keyword = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsGallery(models.Model):
    img_id = models.AutoField(primary_key=True)
    goods_id = models.PositiveIntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    img_desc = models.SmallIntegerField(blank=True, null=True)
    thumb_url = models.CharField(max_length=255, blank=True, null=True)
    img_original = models.CharField(max_length=255, blank=True, null=True)
    external_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_gallery'
