# Generated by Django 5.1.4 on 2025-02-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0004_category_image_projectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='technologies',
            field=models.TextField(blank=True, null=True, verbose_name='Технологии категории'),
        ),
    ]
