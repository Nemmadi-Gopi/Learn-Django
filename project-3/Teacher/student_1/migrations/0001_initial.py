# Generated by Django 2.2 on 2021-11-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'FR'), ('SO', 'SO'), ('JR', 'JR'), ('SR', 'SR'), ('GR', 'GR')], default='FR', max_length=2)),
            ],
        ),
    ]