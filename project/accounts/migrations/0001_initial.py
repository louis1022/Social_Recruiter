# Generated by Django 2.0.6 on 2018-07-16 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_django', '0008_partial_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=64)),
                ('recruiter', models.CharField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth')),
            ],
        ),
    ]
