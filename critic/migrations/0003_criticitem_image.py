# Generated by Django 3.1.2 on 2020-10-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0002_aboutitem_contactitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='criticitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
