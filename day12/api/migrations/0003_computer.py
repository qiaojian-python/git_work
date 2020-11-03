# Generated by Django 2.0.6 on 2020-11-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201103_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('brand', models.CharField(max_length=40, verbose_name='品牌')),
            ],
            options={
                'verbose_name': '电脑',
                'verbose_name_plural': '电脑',
                'db_table': 'bz_computer',
            },
        ),
    ]
