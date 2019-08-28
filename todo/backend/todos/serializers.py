from rest_framework import serializers
from .models import Todo



class TodoSerializer(serializers.ModelDurationField):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo