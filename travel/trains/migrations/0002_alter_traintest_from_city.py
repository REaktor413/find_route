# Generated by Django 4.1.1 on 2022-09-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_name'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city', verbose_name='Из какого города'),
        ),
    ]
