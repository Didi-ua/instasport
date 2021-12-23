from django.contrib import admin

from rangefilter.filters import DateRangeFilter

from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')
    search_fields = ('name',)
    list_filter = (('start', DateRangeFilter),)
