# Generated by Django 4.1.6 on 2023-02-09 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_rename_m_user_tb_borrow_book_m_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_borrow_book',
            old_name='m_name',
            new_name='m_user',
        ),
    ]
