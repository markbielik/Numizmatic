# Generated by Django 4.0.3 on 2022-03-18 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('numiz_app', '0009_alter_coin_dimension_alter_coin_scales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='subject',
            field=models.ForeignKey(help_text='If there is no topic, choose an individual topic', on_delete=django.db.models.deletion.CASCADE, to='numiz_app.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='Temat indywidualny', max_length=250, unique=True, verbose_name='Subject name'),
        ),
    ]
