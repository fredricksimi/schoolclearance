from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class FinanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance
        fields = ('id', 'item_name', 'cash_value')

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'item_name', 'cash_value')

class HostelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hostels
        fields = ('id', 'item_name', 'cash_value')

class CateringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catering
        fields = ('id', 'item_name', 'cash_value')

class Head_of_DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Head_of_Department
        fields = ('id', 'item_name', 'cash_value')

class Dean_of_StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dean_of_Students
        fields = ('id', 'item_name', 'cash_value')

class Dean_of_SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dean_of_School
        fields = ('id', 'item_name', 'cash_value')

class Games_DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games_Department
        fields = ('id', 'item_name', 'cash_value')

class Labs_and_WorkshopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Labs_and_Workshops
        fields = ('id', 'item_name', 'cash_value')

class Registrar_of_AcademicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registrar_of_Academics
        fields = ('id', 'item_name', 'cash_value')

class Finance_OfficerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance_Officer
        fields = ('id', 'item_name', 'cash_value')

