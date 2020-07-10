from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class Head_of_DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Head_of_Department.objects.all()
    serializer_class = Head_of_DepartmentSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Dean_of_SchoolViewSet(viewsets.ModelViewSet):
    queryset = Dean_of_School.objects.all()
    serializer_class = Dean_of_SchoolSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Dean_of_StudentsViewSet(viewsets.ModelViewSet):
    queryset = Dean_of_Students.objects.all()
    serializer_class = Dean_of_StudentsSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Games_DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Games_Department.objects.all()
    serializer_class = Games_DepartmentSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class HostelsViewSet(viewsets.ModelViewSet):
    queryset = Hostels.objects.all()
    serializer_class = HostelsSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Labs_and_WorkshopsViewSet(viewsets.ModelViewSet):
    queryset = Labs_and_Workshops.objects.all()
    serializer_class = Labs_and_WorkshopsSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Registrar_of_AcademicsViewSet(viewsets.ModelViewSet):
    queryset = Registrar_of_Academics.objects.all()
    serializer_class = Registrar_of_AcademicsSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class Finance_OfficerViewSet(viewsets.ModelViewSet):
    queryset = Finance_Officer.objects.all()
    serializer_class = Finance_OfficerSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)