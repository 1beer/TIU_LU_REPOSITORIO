# Generated by Django 2.2.1 on 2019-06-01 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcbolinhas', '0010_auto_20190531_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='produto_pedidodois',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='produto_pedidoquatro',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='produto_pedidotres',
        ),
    ]
