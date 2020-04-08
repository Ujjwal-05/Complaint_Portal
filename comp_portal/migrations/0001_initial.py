# Generated by Django 3.0.1 on 2020-04-04 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('time', models.DateField(auto_now_add=True)),
                ('type', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('problem', models.TextField(max_length=5000)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]