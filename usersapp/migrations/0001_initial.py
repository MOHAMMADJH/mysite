# Generated by Django 4.0.6 on 2022-07-23 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('note', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('date_c', models.DateTimeField(auto_now_add=True, null=True)),
                ('self_d', models.DateTimeField(blank=True, null=True)),
                ('note_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_d', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
