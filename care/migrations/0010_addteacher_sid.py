# Generated by Django 3.1.7 on 2022-07-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0009_remove_addstudent_admissionno'),
    ]

    operations = [
        migrations.AddField(
            model_name='addteacher',
            name='sid',
            field=models.IntegerField(null=True),
        ),
    ]
