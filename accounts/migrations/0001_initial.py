# Generated by Django 2.1.1 on 2018-09-01 17:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_type', models.CharField(choices=[('c', 'Cheques'), ('n', 'Nomina'), ('a', 'Ahorro'), ('i', 'invercion')], default='a', max_length=150)),
                ('balance', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AccountHolder')),
            ],
        ),
    ]
