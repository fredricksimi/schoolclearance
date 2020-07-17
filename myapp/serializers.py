from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class FinanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance
        fields = ('id', 'user', 'item_name', 'cash_value')

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'user', 'item_name', 'cash_value')

class HostelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hostels
        fields = ('id', 'user', 'item_name', 'cash_value')

class CateringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catering
        fields = ('id', 'user', 'item_name', 'cash_value')

class Head_of_DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Head_of_Department
        fields = ('id', 'user', 'item_name', 'cash_value')

class Dean_of_StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dean_of_Students
        fields = ('id', 'user', 'item_name', 'cash_value')

class Dean_of_SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dean_of_School
        fields = ('id', 'user', 'item_name', 'cash_value')

class Games_DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games_Department
        fields = ('id', 'user', 'item_name', 'cash_value')

class Labs_and_WorkshopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Labs_and_Workshops
        fields = ('id', 'user', 'item_name', 'cash_value')

class Registrar_of_AcademicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registrar_of_Academics
        fields = ('id', 'user', 'item_name', 'cash_value')

class Finance_OfficerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance_Officer
        fields = ('id', 'user', 'item_name', 'cash_value')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ('id', 'user', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user