# Generated by Django 2.2 on 2019-05-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_enterprise_whatsapp_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='discounts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
