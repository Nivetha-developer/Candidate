from rest_framework import serializers
from .models import Candidatedirectory

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'
