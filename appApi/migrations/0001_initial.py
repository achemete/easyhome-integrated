# Generated by Django 2.0 on 2018-01-15 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField()),
                ('image', models.URLField()),
                ('image2', models.URLField()),
                ('image3', models.URLField()),
                ('image4', models.URLField()),
                ('visibility', models.BooleanField(default=True)),
                ('guests', models.IntegerField(default=1)),
                ('bedrooms', models.IntegerField(default=1)),
                ('beds', models.IntegerField(default=1)),
                ('bathroom', models.IntegerField(default=1)),
                ('rules', models.TextField(default='')),
                ('extraInfo', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=100)),
                ('kindOfHouse', models.CharField(blank=True, default='', max_length=100)),
                ('locationMap', models.TextField(default='')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('built', models.CharField(blank=True, default='', max_length=100)),
                ('kindOfAttractions', models.CharField(blank=True, default='', max_length=100)),
                ('title1', models.CharField(blank=True, default='', max_length=100)),
                ('title2', models.CharField(blank=True, default='', max_length=100)),
                ('title3', models.CharField(blank=True, default='', max_length=100)),
                ('description1', models.TextField(default='')),
                ('description2', models.TextField(default='')),
                ('description3', models.TextField(default='')),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.URLField()),
                ('image2', models.URLField()),
                ('image3', models.URLField()),
                ('city', models.CharField(default='', max_length=100)),
                ('link', models.URLField()),
                ('locationMap', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('accomodations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Accomodations')),
                ('attractions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Attractions')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('priceRange', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.URLField()),
                ('image2', models.URLField()),
                ('image3', models.URLField()),
                ('city', models.CharField(default='', max_length=100)),
                ('link', models.URLField()),
                ('locationMap', models.TextField()),
                ('kindOfRestaurant', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi', models.BooleanField(default=True)),
                ('shower', models.BooleanField(default=True)),
                ('kitchen', models.BooleanField(default=True)),
                ('surveillanceCamera', models.BooleanField(default=True)),
                ('HeatingSystem', models.BooleanField(default=True)),
                ('Television', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('location', models.CharField(blank=True, default='', max_length=100, unique=True)),
                ('postal', models.CharField(blank=True, default='', max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Restaurant'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Users'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Reviews'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApi.Services'),
        ),
    ]
