from django.db import models

class Finance(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Library(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Hostels(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Catering(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Head_of_Department(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Dean_of_Students(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Dean_of_School(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Games_Department(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Labs_and_Workshops(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)

class Registrar_of_Academics(models.Model):
    item_name = models.CharField(max_length=150)
    cash_value = models.CharField(max_length=50)


class Finance_Officer(models.Model):
    Department = models.OneToOneField(Head_of_Department, on_delete=models.CASCADE)
    School = models.OneToOneField(Dean_of_School, on_delete=models.CASCADE)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    hostels = models.OneToOneField(Hostels, on_delete=models.CASCADE)
    catering = models.OneToOneField(Catering, on_delete=models.CASCADE)
    games = models.OneToOneField(Games_Department, on_delete=models.CASCADE)
    dean_of_students = models.OneToOneField(Dean_of_Students, on_delete=models.CASCADE)
    labs_and_workshops = models.OneToOneField(Labs_and_Workshops, on_delete=models.CASCADE)
    student_finance = models.OneToOneField(Finance, on_delete=models.CASCADE)
    registrar_of_academics = models.OneToOneField(Registrar_of_Academics, on_delete=models.CASCADE)