# Generated by Django 5.0.7 on 2024-08-16 03:30

import ckeditor.fields
import django.db.models.deletion
import hitcount.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Team/images')),
                ('description', models.TextField()),
                ('full_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Blogs/images')),
                ('created_date', models.DateField(auto_now=True)),
                ('author', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category')),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Portfolio/images')),
                ('now_date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=70)),
                ('url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category')),
            ],
        ),
    ]
