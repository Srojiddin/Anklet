# Generated by Django 5.0.1 on 2024-02-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='Слайдер')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slider', models.ManyToManyField(blank=True, to='website.slider', verbose_name='Слайдер')),
            ],
            options={
                'verbose_name': 'Настройка сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
