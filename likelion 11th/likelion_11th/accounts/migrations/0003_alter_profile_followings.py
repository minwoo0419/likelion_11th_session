# Generated by Django 4.2 on 2023-06-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followers', to='accounts.profile'),
        ),
    ]