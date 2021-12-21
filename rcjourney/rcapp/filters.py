import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class PostFilter(django_filters.FilterSet):
    post = CharFilter(field_name='post', lookup_expr='icontains')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user_id', 'date_created', 'tags']
