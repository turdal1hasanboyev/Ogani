# Generated by Django 5.2 on 2025-04-12 09:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_alter_productbanner_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbanner',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
