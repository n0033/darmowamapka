# Generated by Django 3.1.6 on 2021-02-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_mail_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='checkbox_checked',
            field=models.BooleanField(default=False),
        ),
    ]