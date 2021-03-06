# Generated by Django 3.0.7 on 2020-07-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectImage',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='projectName',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
