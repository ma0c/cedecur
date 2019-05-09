# Generated by Django 2.2 on 2019-04-25 04:05

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190421_0336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='discounts',
            options={'verbose_name': 'Discounts', 'verbose_name_plural': 'Discounts'},
        ),
        migrations.AlterModelOptions(
            name='enterprise',
            options={'verbose_name': 'Enterprise', 'verbose_name_plural': 'Enterprise'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategory'},
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('email', models.EmailField(max_length=254)),
                ('title', models.TextField()),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Enterprise')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
            bases=(models.Model, base.models.DisplayFieldsMixin),
        ),
    ]
