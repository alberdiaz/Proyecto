# Generated by Django 4.2.4 on 2023-08-04 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]
