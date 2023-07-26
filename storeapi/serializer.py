from store.models import medicine
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
class medicineserializer(serializers.ModelSerializer):
    class Meta:
        model=medicine
        fields=('id','title','price','status','no_of_pack','exp')
class searchsealizer(serializers.Serializer):
    title=serializers.CharField()
