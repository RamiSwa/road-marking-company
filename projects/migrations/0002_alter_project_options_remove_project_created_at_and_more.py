# Generated by Django 5.0.13 on 2025-03-19 05:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='caption',
        ),
        migrations.AddField(
            model_name='project',
            name='completion_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Completion Date'),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Default project description', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', verbose_name='Featured Image'),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_he',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title_he',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to='projects/gallery/', verbose_name='Gallery Image'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='projects.project'),
        ),
    ]
