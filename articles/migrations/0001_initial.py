# Generated by Django 4.2.5 on 2023-10-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('contenu', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
