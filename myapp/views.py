from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action


class Head_of_DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Head_of_Department.objects.all()
    serializer_class = Head_of_DepartmentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Dean_of_SchoolViewSet(viewsets.ModelViewSet):
    queryset = Dean_of_School.objects.all()
    serializer_class = Dean_of_SchoolSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Dean_of_StudentsViewSet(viewsets.ModelViewSet):
    queryset = Dean_of_Students.objects.all()
    serializer_class = Dean_of_StudentsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Games_DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Games_Department.objects.all()
    serializer_class = Games_DepartmentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class HostelsViewSet(viewsets.ModelViewSet):
    queryset = Hostels.objects.all()
    serializer_class = HostelsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Labs_and_WorkshopsViewSet(viewsets.ModelViewSet):
    queryset = Labs_and_Workshops.objects.all()
    serializer_class = Labs_and_WorkshopsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Registrar_of_AcademicsViewSet(viewsets.ModelViewSet):
    queryset = Registrar_of_Academics.objects.all()
    serializer_class = Registrar_of_AcademicsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class Finance_OfficerViewSet(viewsets.ModelViewSet):
    queryset = Finance_Officer.objects.all()
    serializer_class = Finance_OfficerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthorOrReadOnly,)