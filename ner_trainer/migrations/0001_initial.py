# Generated by Django 2.0.5 on 2018-05-15 03:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import ner_trainer.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100, primary_key=True, serialize=False, validators=[ner_trainer.validators.validate_all_caps])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField(unique=True)),
                ('skipped', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhraseEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start_index', models.SmallIntegerField()),
                ('end_index', models.SmallIntegerField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ner_trainer.Entity')),
                ('phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='ner_trainer.Phrase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
