# Generated by Django 2.2 on 2019-04-02 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['-order']},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='cooking.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='cooking.Recipe'),
        ),
    ]
