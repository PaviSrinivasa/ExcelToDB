# Generated by Django 3.2.4 on 2022-08-01 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genelist', '0003_alter_literature_doi_alter_literature_pmcid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='sourcelink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authF', to='genelist.literature'),
        ),
    ]
