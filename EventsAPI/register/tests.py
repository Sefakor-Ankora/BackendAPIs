from django.test import TestCase
from factory import DjangoModelFactory, Faker
from .factories import RegisterFactory

from ..models import Register
from ..serializers import RegisterSerializer
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class RegisterFactory(DjangoModelFactory):
    fullname = Faker('fullname')
    email = Faker('email')
    phonenumber = Faker('phonenumber')
    ticketnumber = Faker('ticketnumber')
    

    class Meta:
        model = Register




# tests/test_models.py
class RegisterTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        register = RegisterFactory()
        self.assertEqual(str(register), register.name)





# tests/test_serializers.py
class RegisterSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Register object for each field."""
        register = RegisterFactory()
        for field_name in [
            'id', 'fullname', 'email', 'phonenumber', 'ticketnumber'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(register, field_name)




# tests/test_views.py
    def test_post(self):
          """POST to create Registration."""
          data = {
              'fullname': 'New fullname',
              'email': 'New email',
              'phonenumber': 'New phonenumber',
              'tickectnumber': 'New ticketnumber',
              
          }
          self.assertEqual(Register.objects.count(), 0)
          response = self.client.post(self.list_url, data=data)
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(Register.objects.count(), 1)
          events = Register.objects.all().first()
          for field_name in data.keys():
                self.assertEqual(getattr(register, field_name), data[field_name])

      def test_put(self):
          """PUT to update Registration."""
          register = registerFactory()
          data = {
              'fullname': 'New fullname',
              'email': 'New email',
              'phonenumber': 'New phonenumber',
              'tickectnumber': 'New ticketnumber',
          }
          response = self.client.put(
              self.get_detail_url(register.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          register.refresh_from_db()
          for field_name in data.keys():
              self.assertEqual(getattr(register.fullname, data[fullname])

      def test_patch(self):
          """PATCH to update REgistration."""
          register = RegisterFactory()
          data = {'fullname': 'New fullname'}
          response = self.client.patch(
              self.get_detail_url(register.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          register.refresh_from_db()
          self.assertEqual(register.fullname, data['fullname'])

      def test_delete(self):
          """DELETEing is not implemented."""
          register = RegisterFactory()
          response = self.client.delete(self.get_detail_url(register.id))
          self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)