# Generated by Django 4.2.1 on 2024-08-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streeteaseProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='imageUrl',
            field=models.URLField(default='http://example.com/default.jpg'),
        ),
    ]
