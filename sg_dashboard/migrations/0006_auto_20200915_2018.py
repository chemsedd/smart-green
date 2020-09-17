# Generated by Django 3.0.6 on 2020-09-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_dashboard', '0005_daily_real_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_records_stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=20)),
                ('min_temp', models.FloatField(db_column='min_temp')),
                ('avg_temp', models.FloatField(db_column='avg_temp')),
                ('max_temp', models.FloatField(db_column='max_temp')),
                ('min_prec', models.FloatField(db_column='min_prec')),
                ('avg_prec', models.FloatField(db_column='avg_prec')),
                ('max_prec', models.FloatField(db_column='max_prec')),
                ('min_rel_humid', models.FloatField(db_column='min_rel_humid')),
                ('avg_rel_humid', models.FloatField(db_column='avg_rel_humid')),
                ('max_rel_humid', models.FloatField(db_column='max_rel_humid')),
                ('min_pressure', models.FloatField(db_column='min_Pressure')),
                ('avg_pressure', models.FloatField(db_column='avg_Pressure')),
                ('max_pressure', models.FloatField(db_column='max_Pressure')),
            ],
        ),
        migrations.DeleteModel(
            name='Monthly_records',
        ),
    ]
