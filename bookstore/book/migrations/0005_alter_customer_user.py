# Generated by Django 3.2.5 on 2023-08-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_cart_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
