# Generated by Django 4.2.5 on 2023-09-28 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_rename_category_n_operation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='operations.category', verbose_name='Catégorie'),
        ),
    ]