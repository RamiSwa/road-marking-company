# Generated by Django 5.0.13 on 2025-03-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sitesetting_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='additional_locations',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='location',
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='additional_locations_en',
            field=models.TextField(blank=True, null=True, verbose_name='Additional Locations (English)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='additional_locations_he',
            field=models.TextField(blank=True, null=True, verbose_name='Additional Locations (Hebrew)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='company_name_en',
            field=models.CharField(default='ProMark Road Marking', max_length=200, verbose_name='Company Name (English)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='company_name_he',
            field=models.CharField(default='פרומארק סימון כבישים', max_length=200, verbose_name='Company Name (Hebrew)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='footer_text_en',
            field=models.TextField(blank=True, default='Precision & Safety in Every Line', null=True, verbose_name='Footer Text (English)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='footer_text_he',
            field=models.TextField(blank=True, default='דיוק ובטיחות בכל קו', null=True, verbose_name='Footer Text (Hebrew)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='location_en',
            field=models.TextField(default='123 Highway Ave, New York, NY', verbose_name='Main Office Location (English)'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='location_he',
            field=models.TextField(default='רחוב 123 היייווי, ניו יורק, ארה"ב', verbose_name='Main Office Location (Hebrew)'),
        ),
    ]
