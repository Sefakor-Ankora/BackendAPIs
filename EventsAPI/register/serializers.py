from rest_framework import serializers
from register.models import Register
from signup.models import User
from rest_framework.validators import UniqueTogetherValidator



class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        exclude = []
        validators = [
            UniqueTogetherValidator(
                queryset=Register.objects.all(),
                fields=['User', ]
            )
        ]
    
    def validate_events(self, value):
        if value:
            if value.roomcapacity <= Register.objects.count():
                raise serializers.ValidationError(           
                     {"Fully Booked": "All seats have been allocated"})
        return value
        