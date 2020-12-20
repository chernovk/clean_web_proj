# Generated by Django 3.1.2 on 2020-11-19 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('min_coast', models.IntegerField()),
                ('start_at', models.DateTimeField()),
                ('finish_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('sex', models.CharField(blank=True, choices=[('1', 'Мужчина'), ('0', 'Женщина')], max_length=1, null=True)),
                ('city', models.CharField(editable=False, max_length=20)),
                ('age', models.IntegerField(default=18)),
                ('auth_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('price_sale', models.FloatField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegefood.type')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vegefood.product')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vegefood.user')),
            ],
            options={
                'unique_together': {('user_id', 'product')},
            },
        ),
    ]
