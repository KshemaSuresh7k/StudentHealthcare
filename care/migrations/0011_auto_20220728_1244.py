# Generated by Django 3.1.7 on 2022-07-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0010_addteacher_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addteacher',
            name='sid',
        ),
        migrations.AddField(
            model_name='addhealth',
            name='department',
            field=models.CharField(max_length=200, null=True),
        ),
    ]