# Generated by Django 2.2 on 2021-09-17 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('st_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='publishermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('author', models.ManyToManyField(to='student.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_name', models.CharField(max_length=255)),
                ('pages', models.IntegerField(verbose_name='number of pages')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='price')),
                ('release_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.AuthorModel')),
            ],
        ),
    ]
