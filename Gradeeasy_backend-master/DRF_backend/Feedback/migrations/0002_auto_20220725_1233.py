# Generated by Django 3.0.7 on 2022-07-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_model',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
