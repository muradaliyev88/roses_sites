# Generated by Django 2.0.1 on 2018-01-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('pict_id', models.ImageField(upload_to='img', verbose_name='sekil id')),
                ('user_id', models.CharField(max_length=20, verbose_name='user id')),
                ('body', models.TextField(verbose_name='Comments')),
            ],
        ),
    ]
