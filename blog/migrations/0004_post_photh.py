# Generated by Django 2.1.5 on 2019-01-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photh',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]