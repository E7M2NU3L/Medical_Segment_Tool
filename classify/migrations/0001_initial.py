# Generated by Django 3.2.23 on 2024-03-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='./images/classify/')),
            ],
        ),
    ]