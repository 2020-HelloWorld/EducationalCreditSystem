# Generated by Django 4.2.2 on 2023-06-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectattendacerequest',
            name='end',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]