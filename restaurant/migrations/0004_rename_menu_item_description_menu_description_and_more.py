# Generated by Django 4.1.4 on 2023-05-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_item_description',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]