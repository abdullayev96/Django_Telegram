# Generated by Django 4.2.11 on 2024-05-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(unique=True)),
                ('lang_id', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Foydalanuvchi_',
            },
        ),
    ]
