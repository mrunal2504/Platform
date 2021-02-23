# Generated by Django 3.1.6 on 2021-02-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='youtuber',
            old_name='video_urls',
            new_name='video_url',
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(upload_to='media/ytubers/%Y/%m/'),
        ),
    ]
