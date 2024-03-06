# Generated by Django 3.2.23 on 2024-03-06 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermanagement_user', to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContentModeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentmoderation_article', to='news.article')),
            ],
        ),
    ]