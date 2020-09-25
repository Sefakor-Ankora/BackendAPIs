from django.test import TestCase
from factory import DjangoModelFactory, Faker

from ..models import Events
from .factories import EventsFactory
from ..serializers import EventsSerializer
from django.urls import reverse


# Create your tests here.
class EventsFactory(DjangoModelFactory):
    speaker_name = Faker('speaker_name')
    topic = Faker('topic')
    time_scheduled = Faker('time_scheduled')
    time = Faker('time')
    room_capacity = Faker('room_capacity')
    description = Faker('description')

    

    class Meta:
        model = Events




# tests/test_models.py
class EventsTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        events = EventsFactory()
        self.assertEqual(str(events), events.name)



# tests/test_serializers.py
class EventsSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Events object for each field."""
        events = EventsFactory()
        for field_name in [
            'id', 'speaker_name', 'topic', 'time_scheduled', 'time', 'room_capacity',
            'description'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(events, field_name)




# tests/test_views.py

def test_post(self):
          """POST to create an Event."""
          data = {
              'speakr_name': 'New speaker_name',
              'topic': 'New topic',
              'time_scheduled': 'New time_scheduled',
              'time': 'New time',
              'room_capacity': 'New room_capacity',
              'description': 'New description',
          }
          self.assertEqual(Events.objects.count(), 0)
          response = self.client.post(self.list_url, data=data)
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(Events.objects.count(), 1)
          events = Events.objects.all().first()
          for field_name in data.keys():
                self.assertEqual(getattr(events, field_name), data[field_name])

      def test_put(self):
          """PUT to update an Event."""
          events = EventsFactory()
          data = {
              'speakr_name': 'New speaker_name',
              'topic': 'New topic',
              'time_scheduled': 'New time_scheduled',
              'time': 'New time',
              'room_capacity': 'New room_capacity',
              'description': 'New description',
          }
          response = self.client.put(
              self.get_detail_url(events.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          company.refresh_from_db()
          for field_name in data.keys():
              self.assertEqual(getattr(events, field_name), data[field_name])

      def test_patch(self):
          """PATCH to update an Event."""
          events = EventsFactory()
          data = {'speaker_name': 'New speaker_name'}
          response = self.client.patch(
              self.get_detail_url(events.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          events.refresh_from_db()
          self.assertEqual(events.speaker_name, data['speaker_name'])

      def test_delete(self):
          """DELETEing is not implemented."""
          events = EventsFactory()
          response = self.client.delete(self.get_detail_url(events.id))
          self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)