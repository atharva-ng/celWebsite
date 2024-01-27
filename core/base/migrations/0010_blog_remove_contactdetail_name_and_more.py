# Generated by Django 4.2.4 on 2024-01-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_blog_delete_coordi_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blogImages/')),
                ('link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='name',
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='firstName',
            field=models.CharField(default='defaultName', max_length=50),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='lastName',
            field=models.CharField(default='defaultName', max_length=50),
        ),
    ]
