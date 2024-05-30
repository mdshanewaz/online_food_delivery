# Generated by Django 5.0 on 2024-05-30 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubscriptionApp', '0006_alter_packagemodel_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lunch_off', models.BooleanField(default=False)),
                ('dinner_off', models.BooleanField(default=False)),
                ('date_creted', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscriptionApp.packagemodel')),
            ],
            options={
                'verbose_name_plural': 'Meals',
            },
        ),
    ]
