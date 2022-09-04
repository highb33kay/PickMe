import django_filters
# Create your views here.

from models import *

class PickFilter(django_filters.FilterSet):
    class Meta:
        model = PickUpLine
        fields = '__all__'