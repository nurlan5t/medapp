from rest_framework import serializers
from api.models import Patient, Diagnose


# Serializer for diagnose
class DiagnoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = ('title', 'description')


# Serializer for Patient
class PatientSerializer(serializers.ModelSerializer):
    diagnoses = DiagnoseSerializer(read_only=True, many=True)

    class Meta:
        model = Patient
        fields = '__all__'


# Serializer for login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
