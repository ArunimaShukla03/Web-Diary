# Generated by Django 4.1.5 on 2023-04-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mood',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
    ]