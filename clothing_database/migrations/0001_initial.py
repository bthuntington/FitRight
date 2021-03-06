# Generated by Django 2.1.3 on 2018-12-07 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClothingPreferance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=25, null=True)),
                ('pattern', models.CharField(blank=True, max_length=25, null=True)),
                ('fit', models.CharField(blank=True, max_length=25, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('lightness', models.IntegerField(blank=True, null=True)),
                ('price_min', models.IntegerField(blank=True, null=True)),
                ('price_max', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clothing_preferance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'profile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('val', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LowerBody',
            fields=[
                ('lb', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='lb_set', serialize=False, to='clothing_database.Profile')),
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
                'db_table': 'lower_body',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='brand_set', serialize=False, to='clothing_database.Profile')),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('pattern', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('lightness', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_line',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UpperBody',
            fields=[
                ('ub', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='ub_set', serialize=False, to='clothing_database.Profile')),
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
                'db_table': 'upper_body',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='color_set', serialize=False, to='clothing_database.ProductLine')),
                ('lightness', models.IntegerField(blank=True, null=True)),
                ('color_type', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('m', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='m_set', serialize=False, to='clothing_database.ProductLine')),
                ('material_type', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='p_set', serialize=False, to='clothing_database.ProductLine')),
                ('pattern_type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pattern',
                'managed': False,
            },
        ),
    ]
