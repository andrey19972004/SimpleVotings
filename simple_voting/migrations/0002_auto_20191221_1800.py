# Generated by Django 3.0 on 2019-12-21 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple_voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='question',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_voting.Option')),
            ],
        ),
    ]