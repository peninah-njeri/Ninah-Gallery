# Generated by Django 2.2.7 on 2019-11-10 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Location'),
        ),
    ]