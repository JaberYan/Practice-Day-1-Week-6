# Generated by Django 4.2.7 on 2023-12-26 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0004_alter_moneytransfer_account_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneytransfer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userbankaccount'),
        ),
    ]
