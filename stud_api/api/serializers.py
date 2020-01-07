from rest_framework import serializers
from .models import stud

class studSerializer(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = ['id', 'name', 'age', 'std']


class stud2Serializer(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = ('id', 'name', 'age', 'std')