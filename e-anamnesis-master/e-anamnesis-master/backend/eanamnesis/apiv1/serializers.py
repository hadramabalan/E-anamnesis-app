from apiv1.models import Patient
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Patient
        fields = ["user", "degree_prefix", "degree_postfix", "birth_cert_num", "birth_date", "post_address", "zip", "phone", "email"]