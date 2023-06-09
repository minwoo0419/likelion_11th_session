# Generated by Django 4.2 on 2023-05-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='main.tag'),
        ),
    ]
