# Generated by Django 2.1.2 on 2018-10-20 10:53

from django.db import migrations

def set_room_position_value(apps, schema_editor):
    Topic = apps.get_model('mainapp', 'Topic')
    Room = apps.get_model('mainapp', 'Room')

    for topic in Topic.objects.all():
        if Room.objects.filter(name="general", topic=topic).exists():
            room_general = Room.objects.get(name="general", topic=topic)
            room_general.position = 1
            room_general.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_room_position'),
    ]

    operations = [
        migrations.RunPython(set_room_position_value),
    ]
