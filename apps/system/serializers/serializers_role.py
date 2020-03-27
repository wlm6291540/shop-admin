from rest_framework import serializers
from rest_framework.fields import empty

from system.models import Role, User, Menu


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'desc', 'users']


class RoleBindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id']


# 角色绑定用户
class RoleUserSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.username

    def get_value(self, obj):
        return obj.id

    class Meta:
        model = User
        fields = ['value', 'title']


# 角色绑定菜单
class RoleMenuSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, data=empty, **kwargs):
        self.instance = instance
        if data is not empty:
            self.initial_data = data
        self.role_menus = kwargs.pop('role_menus', [])
        self.partial = kwargs.pop('partial', False)
        self._context = kwargs.pop('context', {})
        kwargs.pop('many', None)
        super().__init__(**kwargs)

    checked = serializers.SerializerMethodField()

    def get_checked(self, obj):
        children = len(obj.children.values('id'))
        if obj in self.role_menus and obj.parent and obj.parent.parent is not None:
            return True
        if obj in self.role_menus and obj.parent and obj.parent.parent is None and children <= 0:
            return True
        if obj in self.role_menus and obj.parent is None and children <= 0:
            return True
        return False

    class Meta:
        model = Menu
        fields = ['id', 'title', 'parent', 'checked', 'children']


# 角色绑定菜单
class RoleMenuBindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id']
