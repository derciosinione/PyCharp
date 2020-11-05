# Generated by Django 2.2.4 on 2020-09-27 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_perfil_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followersrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tipoUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.TipoUser'),
        ),
    ]