# Generated by Django 5.0.7 on 2024-07-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carts/')),
                ('name', models.CharField(max_length=255)),
                ('size', models.FloatField()),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
    ]