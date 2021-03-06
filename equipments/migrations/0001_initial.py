# Generated by Django 2.0.5 on 2018-05-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('eq_type', models.IntegerField()),
                ('owner', models.CharField(max_length=20)),
                ('state', models.IntegerField()),
                ('due', models.DateTimeField()),
                ('borrower', models.CharField(max_length=20)),
                ('remark', models.TextField()),
            ],
        ),
    ]
