# Generated by Django 3.0.8 on 2020-07-07 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dean_of_School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dean_of_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Games_Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Head_of_Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Labs_and_Workshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registrar_of_Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('cash_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Finance_Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Head_of_Department')),
                ('School', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Dean_of_School')),
                ('catering', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Catering')),
                ('dean_of_students', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Dean_of_Students')),
                ('games', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Games_Department')),
                ('hostels', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Hostels')),
                ('labs_and_workshops', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Labs_and_Workshops')),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Library')),
                ('registrar_of_academics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Registrar_of_Academics')),
                ('student_finance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Finance')),
            ],
        ),
    ]
