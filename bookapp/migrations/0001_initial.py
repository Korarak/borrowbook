# Generated by Django 4.1.6 on 2023-02-08 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_book',
            fields=[
                ('b_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=60)),
                ('b_writer', models.CharField(max_length=50, null=True)),
                ('b_category', models.IntegerField()),
                ('b_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_member',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_user', models.CharField(max_length=50, null=True)),
                ('m_pass', models.CharField(max_length=100, null=True)),
                ('m_name', models.CharField(max_length=50, null=True)),
                ('m_phone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tb_borrow_book',
            fields=[
                ('br_id', models.AutoField(primary_key=True, serialize=False)),
                ('br_date_br', models.DateField()),
                ('br_date_rt', models.DateField()),
                ('br_fine', models.IntegerField()),
                ('b_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.tb_book')),
                ('m_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.tb_member')),
            ],
        ),
    ]
