# Generated by Django 3.1.7 on 2022-07-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0005_addhealth_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addhealth',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='addstudent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='addteacher',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='crud',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
