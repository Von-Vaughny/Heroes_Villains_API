from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        field = ["id", "name", "alter_ego", "primary_ability", "secondary_ability", "catch_phrase", "super_type_id"]
        depth = 1