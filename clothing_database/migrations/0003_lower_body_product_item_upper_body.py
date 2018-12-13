# Generated by Django 2.1.3 on 2018-12-12 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_database', '0002_productitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='lower_body',
            fields=[
                ('lb', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='lb_set', serialize=False, to='clothing_database.Profile')),
                ('company', models.IntegerField(blank=True, null=True)),
                ('waist', models.FloatField(blank=True, null=True)),
                ('hips', models.FloatField(blank=True, null=True)),
                ('thigh', models.FloatField(blank=True, null=True)),
                ('knee', models.FloatField(blank=True, null=True)),
                ('calf', models.FloatField(blank=True, null=True)),
                ('instep', models.FloatField(blank=True, null=True)),
                ('side_to_knee', models.FloatField(blank=True, null=True)),
                ('side_length', models.FloatField(blank=True, null=True)),
                ('crotch_depth', models.FloatField(blank=True, null=True)),
                ('crotch_length', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lower_body',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='product_item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_id', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('pattern', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('lightness', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='upper_body',
            fields=[
                ('ub', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='ub_set', serialize=False, to='clothing_database.Profile')),
                ('company', models.IntegerField(blank=True, null=True)),
                ('size_def', models.CharField(blank=True, max_length=2, null=True)),
                ('chest', models.FloatField(blank=True, null=True)),
                ('neck_to_wrist', models.FloatField(blank=True, null=True)),
                ('back_to_waist', models.FloatField(blank=True, null=True)),
                ('cross_back', models.FloatField(blank=True, null=True)),
                ('hand_cicurm', models.FloatField(blank=True, null=True)),
                ('wrist_cicurm', models.FloatField(blank=True, null=True)),
                ('hand_length', models.FloatField(blank=True, null=True)),
                ('arm_length', models.FloatField(blank=True, null=True)),
                ('upper_arm', models.FloatField(blank=True, null=True)),
                ('arm_hole_depth', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'upper_body',
                'managed': False,
            },
        ),
    ]
