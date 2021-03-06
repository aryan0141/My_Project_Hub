# Generated by Django 3.0.6 on 2020-05-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=200)),
                ('main_desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('date', models.DateField()),
            ],
        ),
    ]
