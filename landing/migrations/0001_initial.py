# Generated by Django 3.0 on 2019-12-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Section')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('image', models.ImageField(upload_to='weatherapp_images/')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ['title'],
            },
        ),
    ]
