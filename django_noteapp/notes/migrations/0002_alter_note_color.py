# Generated by Django 5.0.9 on 2024-11-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(blank=True, default='', max_length=7, null=True),
        ),
    ]