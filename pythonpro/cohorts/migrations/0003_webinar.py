# Generated by Django 2.0.6 on 2018-06-05 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0002_liveclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('speaker', models.CharField(max_length=50)),
                ('speaker_title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('vimeo_id', models.CharField(blank=True, max_length=11)),
                ('start', models.DateTimeField()),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cohorts.Cohort')),
            ],
        ),
    ]
