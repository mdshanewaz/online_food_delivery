# Generated by Django 5.0 on 2024-05-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubscriptionApp', '0005_rename_created_packagemodel_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemodel',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]