# Generated by Django 3.1.7 on 2021-05-08 19:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_auto_20210508_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
