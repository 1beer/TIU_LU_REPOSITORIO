# Generated by Django 2.2.1 on 2019-06-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcbolinhas', '0011_auto_20190531_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='produto_pedido',
            new_name='produto_pedidocinco',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='produto_pedidodois',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='produto_pedidoquatro',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='produto_pedidotres',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
