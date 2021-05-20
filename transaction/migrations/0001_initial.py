# Generated by Django 3.2.3 on 2021-05-20 16:18

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
                ('source', models.CharField(max_length=255, null=True)),
                ('destination', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
    ]
