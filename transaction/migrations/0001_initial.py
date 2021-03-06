# Generated by Django 3.2.3 on 2021-05-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.BigIntegerField()),
                ('destination', models.BigIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('additional', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
