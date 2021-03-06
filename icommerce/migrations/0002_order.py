# Generated by Django 3.1.1 on 2020-09-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(max_length=20)),
                ('itemsJson', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
