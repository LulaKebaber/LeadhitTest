from rest_framework import serializers
from .models import FormTemplate


class GetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = '__all__'


class AddFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = '__all__'
