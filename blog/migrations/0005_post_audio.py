# Generated by Django 3.0.6 on 2020-05-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200514_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.URLField(default='spotify:episode:0Vbl7RvX3KE0lSkRmy9Wjj'),
        ),
    ]
