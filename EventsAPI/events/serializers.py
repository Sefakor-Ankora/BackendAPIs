from rest_framework import serializers
from events.models import Events



class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('id', 
        'title',
         'speaker_name', 
         'topic', 
         'time_scheduled',
          'schedule', 
          'room_capacity', 
          'description', 
          'date',
          'image')