# Generated by Django 2.1.2 on 2018-12-11 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestAuctionPortal', '0012_test_next_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='userprofile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Profile'),
        ),
    ]
