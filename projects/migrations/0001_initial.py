# Generated by Django 5.0.13 on 2025-03-18 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=200, verbose_name='Title (English)')),
                ('title_he', models.CharField(max_length=200, verbose_name='Title (Hebrew)')),
                ('slug', models.SlugField(unique=True)),
                ('description_en', models.TextField(verbose_name='Description (English)')),
                ('description_he', models.TextField(verbose_name='Description (Hebrew)')),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')], default='ongoing', max_length=10)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='projects/main/', verbose_name='Main Image')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title (SEO)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Description (SEO)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/gallery/', verbose_name='Additional Image')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.project')),
            ],
        ),
    ]
