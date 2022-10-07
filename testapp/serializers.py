from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from testapp.models import Employ

class EmployeSerilaizers(serializers.ModelSerializer):
    class Meta:
        model=Employ
        fields='__all__'
    