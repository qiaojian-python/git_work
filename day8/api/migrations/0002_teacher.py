# Generated by Django 2.0.6 on 2020-10-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default=0)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.ImageField(default='teacher/1.jpg', upload_to='teacher/')),
                ('school', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'db_table': 'bz_teacher',
            },
        ),
    ]
