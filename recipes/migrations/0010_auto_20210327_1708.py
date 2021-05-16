# Generated by Django 2.0.2 on 2018-03-27 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20180327_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='reason',
            field=models.CharField(choices=[('Мат', 'ненормативная лексика'), ('Оскорбления', 'оскорбления'), ('Другое', 'другое')], default='Другое', max_length=1),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='dish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]