from rest_framework import serializers
from api.models import Patient, Diagnose


class DiagnoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = ('title', 'description')


class PatientSerializer(serializers.ModelSerializer):
    diagnoses = DiagnoseSerializer(read_only=True, many=True)

    class Meta:
        model = Patient
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
