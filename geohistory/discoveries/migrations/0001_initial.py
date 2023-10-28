# Generated by Django 4.2.4 on 2023-10-18 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2023, 10, 18, 11, 13, 40, 658228, tzinfo=datetime.timezone.utc), verbose_name='Год открытия')),
                ('status', models.IntegerField(choices=[(1, 'Введён'), (2, 'В работе'), (3, 'Завершён'), (4, 'Отменён'), (5, 'Удалён')], default=1, max_length=100, verbose_name='Статус')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 10, 18, 11, 13, 40, 658228, tzinfo=datetime.timezone.utc), verbose_name='Дата создания')),
                ('date_of_formation', models.DateTimeField(default=datetime.datetime(2023, 10, 18, 11, 13, 40, 658228, tzinfo=datetime.timezone.utc), verbose_name='Дата формирования')),
                ('date_complete', models.DateTimeField(default=datetime.datetime(2023, 10, 18, 11, 13, 40, 658228, tzinfo=datetime.timezone.utc), verbose_name='Дата завершения')),
            ],
            options={
                'verbose_name': 'Открытие',
                'verbose_name_plural': 'Открытия',
            },
        ),
        migrations.CreateModel(
            name='Pioneer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('status', models.IntegerField(choices=[(1, 'Действует'), (2, 'Удалена')], default=1, max_length=100, verbose_name='Статус')),
                ('description', models.TextField(max_length=500, verbose_name='Биография')),
                ('image', models.ImageField(default='pioneers/default.jpg', upload_to='pioneers', verbose_name='Фото')),
                ('date_birthday', models.IntegerField(default=1800, verbose_name='Год рождения')),
                ('date_death', models.IntegerField(default=1900, verbose_name='Год смерти')),
            ],
            options={
                'verbose_name': 'Первооткрыватель',
                'verbose_name_plural': 'Первооткрыватели',
            },
        ),
    ]
