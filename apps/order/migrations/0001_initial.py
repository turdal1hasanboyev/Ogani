# Generated by Django 5.2 on 2025-04-11 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Completed'), (2, 'Canceled')], default=0)),
                ('phone_number', models.CharField(db_index=True, max_length=15)),
                ('full_name', models.CharField(db_index=True, max_length=225)),
                ('notes', models.TextField(blank=True, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
