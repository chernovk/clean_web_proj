# Generated by Django 3.1.2 on 2020-11-09 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegefood', '0004_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegefood.type'),
        ),
    ]
