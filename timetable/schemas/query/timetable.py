import graphene
import django_filters
from graphene import relay
from graphene_django import DjangoObjectType
from django_filters import rest_framework as filter

from timetable.models import Timetable


class TimeTableFilter(filter.FilterSet):
    date_before = django_filters.DateFilter(field_name='start', lookup_expr='lte')
    date_after = django_filters.DateFilter(field_name='start', lookup_expr='gte')

    class Meta:
        model = Timetable
        fields = ('start',)


class TimetableNode(DjangoObjectType):
    start = graphene.String()
    end = graphene.String()

    class Meta:
        model = Timetable
        fields = '__all__'
        filterset_class = TimeTableFilter
        interfaces = (relay.Node, )

    def resolve_start(self, info):
        return self.start.strftime('%d-%m-%Y %H:%M:%S')

    def resolve_end(self, info):
        return self.end.strftime('%d-%m-%Y %H:%M:%S')

