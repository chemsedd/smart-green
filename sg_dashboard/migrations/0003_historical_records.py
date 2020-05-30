# Generated by Django 3.0.5 on 2020-05-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_dashboard', '0002_auto_20200517_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historical_records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=20)),
                ('day', models.IntegerField(db_column='Day')),
                ('min_temp', models.FloatField(db_column='Min Temperature')),
                ('avg_temp', models.FloatField(db_column='Avg Temperature')),
                ('max_temp', models.FloatField(db_column='Max Temperature')),
                ('prec', models.FloatField(db_column='Precipitation')),
                ('rel_humid', models.FloatField(db_column='Relative Humidity')),
                ('pressure', models.FloatField(db_column='Pressure')),
            ],
        ),
    ]
