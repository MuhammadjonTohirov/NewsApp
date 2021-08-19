# Generated by Django 3.2.3 on 2021-05-27 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lnews', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lnews.basemodel')),
                ('title', models.TextField(verbose_name='Country name')),
                ('flag', models.ImageField(help_text='A flag of the country', upload_to='', verbose_name='Flag')),
            ],
            bases=('lnews.basemodel',),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='title',
            field=models.TextField(help_text='Category title', verbose_name='Category name'),
        ),
    ]