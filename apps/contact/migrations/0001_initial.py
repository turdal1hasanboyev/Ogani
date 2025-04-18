# Generated by Django 5.2 on 2025-04-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
