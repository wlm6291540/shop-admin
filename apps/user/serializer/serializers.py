import time

from rest_framework import serializers

from user.models import Users


class ShopUserListSerializer(serializers.ModelSerializer):
    auth_status_desc = serializers.SerializerMethodField()
    reg_time_format = serializers.SerializerMethodField()

    def get_auth_status_desc(self, obj):
        return obj.get_auth_status_display()

    def get_reg_time_format(self, obj):
        time_array = time.localtime(obj.reg_time)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'company_name', 'user_money',
                  'frozen_money', 'reg_time', 'reg_time_format', 'auth_status', 'auth_status_desc', 'private_key', 'public_key']


class ShopUserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name', 'company_name', 'password', 'user_money', 'frozen_money', 'auth_status']


class ShopUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name', 'company_name', 'user_money', 'frozen_money', 'auth_status']


class ShopUserChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_money']
