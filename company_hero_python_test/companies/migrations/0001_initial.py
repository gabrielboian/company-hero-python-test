# Generated by Django 3.2.4 on 2021-06-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'db_table': 'company',
            },
        ),
    ]