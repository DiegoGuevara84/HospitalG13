# Generated by Django 4.1.1 on 2022-09-29 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Usuario')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('perfil', models.CharField(max_length=30, verbose_name='Perfil')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=35, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=35, verbose_name='Telefono')),
                ('genero', models.CharField(max_length=35, null=True, verbose_name='Genero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=35, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=35, verbose_name='Ciudad')),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Signos_Vitales',
            fields=[
                ('sv_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID signos vitales')),
                ('sv_fecha_hora', models.DateTimeField(auto_now=True, verbose_name='Fecha hora signos vitales')),
                ('sv_oximetria', models.FloatField(null=True, verbose_name='Oximetría')),
                ('sv_f_respiratoria', models.FloatField(null=True, verbose_name='Frecuencia respiratoria')),
                ('sv_f_cardiaca', models.FloatField(null=True, verbose_name='Frecuencia cardíaca')),
                ('sv_temperatura', models.FloatField(null=True, verbose_name='Temperatura')),
                ('sv_presion_arterial', models.FloatField(null=True, verbose_name='Presión arterial')),
                ('sv_glicemia', models.FloatField(null=True, verbose_name='Glicemia')),
                ('sv_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signos_vitales', to='appHG13.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_salud',
            fields=[
                ('id_Psalud', models.AutoField(primary_key=True, serialize=False, verbose_name='ID personal salud')),
                ('rol', models.CharField(max_length=35, verbose_name='Rol')),
                ('especialidad', models.CharField(max_length=35, verbose_name='Especialidad')),
                ('username', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='Psalud', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_Psalud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente', to='appHG13.personal_salud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('hc_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id historia clinica')),
                ('hc_Fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha historia clinica')),
                ('hc_Entorno', models.CharField(max_length=50, verbose_name='Entorno')),
                ('hc_Diagnostico', models.CharField(max_length=100, verbose_name='Diagnsstico')),
                ('hc_Recomendaciones', models.CharField(max_length=200, verbose_name='Recomendaciones')),
                ('hc_Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_clinica', to='appHG13.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id_f', models.AutoField(primary_key=True, serialize=False, verbose_name='ID familiar')),
                ('correo_f', models.EmailField(max_length=50, unique=True, verbose_name='Correo familiar')),
                ('parentesco_f', models.CharField(max_length=20, verbose_name='Parentesco familiar')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='appHG13.paciente')),
                ('username_f', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
