from django.contrib import admin
from .models import Events

# Register your models here.
#admin.site.register(Events)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
      fields = ('title', 'speaker_name', 'topic', 'description', 'date', 'schedule', 'room_capacity', 'image')
      list_display = ( 'title', 'date', 'speaker_name', 'topic', 'schedule', 'room_capacity', 'description','image' )
      ordering = ('title',)
      search_fields = ('speaker_name',)


