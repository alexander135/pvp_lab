# Generated by Django 2.0.2 on 2018-03-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20180327_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='reason',
            field=models.CharField(choices=[('Мат', 'ненормативная лексика'), ('Оскорбления', 'оскорбления'), ('Другое', 'другое')], default='Другое', max_length=255),
        ),
    ]