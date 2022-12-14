# Generated by Django 4.1.1 on 2022-09-12 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_name'),
        ('trains', '0002_alter_traintest_from_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='Из какого города'),
        ),
        migrations.AlterField(
            model_name='train',
            name='to_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='В какой город'),
        ),
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city', verbose_name='Из какого города'),
        ),
    ]
