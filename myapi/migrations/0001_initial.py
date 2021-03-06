# Generated by Django 3.1.5 on 2021-01-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='nom du client')),
                ('adresse', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ville', models.CharField(max_length=64, verbose_name='ville')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=64, verbose_name='Libelle produit')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
