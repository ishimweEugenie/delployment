# Generated by Django 3.2.9 on 2021-12-04 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('co_time', models.DateTimeField(auto_now=True)),
                ('ingredients', models.TextField(blank=True)),
                ('pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Di_name', models.CharField(max_length=50)),
                ('provinse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_name', models.CharField(max_length=50)),
                ('disstrict', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('dishe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dishes', to='Restaurant.dishes')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='address', to='Restaurant.district')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='address', to='Restaurant.sector')),
            ],
        ),
    ]
