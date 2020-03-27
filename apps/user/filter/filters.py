from django_filters import rest_framework as filters

from user.models import Users


class UsersFilter (filters.FilterSet):
    """用户的过滤类"""
    # 区间查询,指定区间的最大最小值
    reg_time = filters.RangeFilter()

    class Meta:
        model = Users
        fields = ('reg_time', 'company_name', 'user_name', 'auth_status')
