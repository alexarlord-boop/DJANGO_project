# Generated by Django 3.1.6 on 2021-02-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('coords', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('user_skill', models.IntegerField()),
                ('enviroment_chars', models.IntegerField()),
                ('extreme', models.IntegerField()),
            ],
        ),
    ]