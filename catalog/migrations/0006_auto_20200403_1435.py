# Generated by Django 2.2.1 on 2020-04-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200403_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagebook',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('French', 'French'), ('Yoruba', 'Yoruba')], default='e', max_length=10),
        ),
    ]