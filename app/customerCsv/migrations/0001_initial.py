# Generated by Django 3.2.9 on 2021-12-05 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField()),
                ('customer_name_kana', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('birth', models.CharField(max_length=200)),
                ('pref', models.CharField(max_length=200)),
            ],
        ),
    ]