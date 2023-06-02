# Generated by Django 4.2.1 on 2023-06-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_integration', '0001_initial'),
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledpost',
            name='social_media_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media_integration.socialmediaaccount'),
        ),
        migrations.DeleteModel(
            name='SocialMediaAccount',
        ),
    ]
