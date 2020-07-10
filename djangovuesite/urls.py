from django.contrib import admin
from django.urls import path, include
from myapp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('deanschool', Dean_of_SchoolViewSet)
router.register('hod', Head_of_DepartmentViewSet)
router.register('dean-of-students', Dean_of_StudentsViewSet)
router.register('gamesdepartment', Games_DepartmentViewSet)
router.register('hostels', HostelsViewSet)
router.register('catering', CateringViewSet)
router.register('labs', Labs_and_WorkshopsViewSet)
router.register('registrar', Registrar_of_AcademicsViewSet)
router.register('financeofficer', Finance_OfficerViewSet)
router.register('finance', FinanceViewSet)
router.register('library', LibraryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

