from rest_framework import serializers

from system.models import Menu


class MenuTreeThirdSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    def get_label(self, obj):
        return obj.title

    class Meta:
        model = Menu
        fields = '__all__'


class MenuTreeSecondSerializer(serializers.ModelSerializer):
    children = MenuTreeThirdSerializer(many=True)
    label = serializers.SerializerMethodField()

    def get_label(self, obj):
        return obj.title

    class Meta:
        model = Menu
        fields = '__all__'


class MenuTreeSerializer(serializers.ModelSerializer):
    children = MenuTreeSecondSerializer(many=True)
    label = serializers.SerializerMethodField()

    def get_label(self, obj):
        return obj.title

    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()

    def get_type_name(self, obj):
        return obj.get_type_display()

    def get_parent_name(self, obj):
        if obj.parent:
            return obj.parent.title
        return None

    class Meta:
        model = Menu
        fields = '__all__'

