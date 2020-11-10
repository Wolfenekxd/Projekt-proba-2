# Generated by Django 3.1.3 on 2020-11-09 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Poll_question', models.TextField(max_length=256)),
                ('Date_of_poll', models.DateField()),
                ('End_of_poll', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='single_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer_text', models.TextField(max_length=256)),
                ('result', models.IntegerField()),
                ('Poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.polls')),
            ],
        ),
        migrations.CreateModel(
            name='voted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted', models.BooleanField(default=False)),
                ('Poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.polls')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('Poll_id', 'user_id')},
            },
        ),
    ]
