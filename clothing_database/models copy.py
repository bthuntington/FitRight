# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClothingPreferance(models.Model):
    profile = models.OneToOneField('Profile', models.DO_NOTHING, related_name="profile_set")
    profile_name = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_name',related_name="user_name_set")
    material = models.CharField(max_length=25, blank=True, null=True)
    pattern = models.CharField(max_length=25, blank=True, null=True)
    fit = models.CharField(max_length=25, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    lightness = models.IntegerField(blank=True, null=True)
    price_min = models.IntegerField(blank=True, null=True)
    price_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clothing_preferance'
        unique_together = (('profile', 'profile_name'),)


class Color(models.Model):
    c = models.OneToOneField('ProductItem', models.DO_NOTHING, primary_key=True, related_name="color_set")
    c_name = models.ForeignKey('ProductItem', models.DO_NOTHING, db_column='c_name', blank=True, null=True, related_name="color_name_set")
    lightness = models.IntegerField(blank=True, null=True)
    color_type = models.CharField(max_length=17)


    class Meta:
        managed = False
        db_table = 'color'
        unique_together = (('c', 'color_type'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LowerBody(models.Model):
    lb = models.OneToOneField('Profile', models.DO_NOTHING, primary_key=True, related_name="lb_set")
    lb_name = models.ForeignKey('Profile', models.DO_NOTHING, db_column='lb_name', related_name="lb_name_set")
    size_def = models.CharField(max_length=2, blank=True, null=True)
    chest = models.FloatField(blank=True, null=True)
    neck_to_wrist = models.FloatField(blank=True, null=True)
    back_to_waist = models.FloatField(blank=True, null=True)
    cross_back = models.FloatField(blank=True, null=True)
    hand_cicurm = models.FloatField(blank=True, null=True)
    wrist_cicurm = models.FloatField(blank=True, null=True)
    hand_length = models.FloatField(blank=True, null=True)
    arm_length = models.FloatField(blank=True, null=True)
    upper_arm = models.FloatField(blank=True, null=True)
    arm_hole_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lower_body'
        unique_together = (('lb', 'lb_name'),)


class Material(models.Model):
    m = models.OneToOneField('ProductItem', models.DO_NOTHING, related_name="m_set", primary_key=True)
    m_name = models.ForeignKey('ProductItem', models.DO_NOTHING, related_name="m_name", db_column='m_name', blank=True, null=True)
    material_type = models.CharField(max_length=17)

    class Meta:
        managed = False
        db_table = 'material'
        unique_together = (('m', 'material_type'),)

    # def __str__(self):
    #     return "%s" % (self.m_name)

class Pattern(models.Model):
    p = models.OneToOneField('ProductItem', models.DO_NOTHING, primary_key=True, related_name="p_set")
    p_name = models.ForeignKey('ProductItem', models.DO_NOTHING, db_column='p_name', blank=True, null=True, related_name="product_name_set")
    pattern_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pattern'
        unique_together = (('p', 'pattern_type'),)

    # def __str__(self):
  #     return "%s" % (self.p_name)

COLOR_CHOICES = (
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ( 'black', 'Black'),
    ('red', 'Red'),
    ('brown', 'Brown'),
    ('white', 'White'),
    ('grey', 'Grey'),
    ('blue', 'Blue')
    )
class ProductItem(models.Model):
    brand_id = models.IntegerField(primary_key=True, blank=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    pattern = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    lightness = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return "%s" % (self.color)

    class Meta:
        managed = False
        db_table = 'product_item'
        unique_together = (('brand_id', 'brand_name'),)


class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    profile_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'
        unique_together = (('profile_id', 'profile_name'),)

    # def __str__(self):
    #     return "%s %s" % (self.first_name, self.last_name)


class UpperBody(models.Model):
    ub = models.OneToOneField(Profile, models.DO_NOTHING, primary_key=True, related_name="ub_set")
    ub_name = models.ForeignKey(Profile, models.DO_NOTHING, db_column='ub_name')
    waist = models.FloatField(blank=True, null=True)
    hips = models.FloatField(blank=True, null=True)
    thigh = models.FloatField(blank=True, null=True)
    knee = models.FloatField(blank=True, null=True)
    calf = models.FloatField(blank=True, null=True)
    instep = models.FloatField(blank=True, null=True)
    side_to_knee = models.FloatField(blank=True, null=True)
    side_length = models.FloatField(blank=True, null=True)
    crotch_depth = models.FloatField(blank=True, null=True)
    crotch_length = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upper_body'
        unique_together = (('ub', 'ub_name'),)
