# Generated by Django 5.0.3 on 2024-06-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resortapp', '0002_members_alter_contacts_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(choices=[('Malika', 'Malika'), ('Aimi', 'Aimi'), ("Ja'kote", "Ja'kote")], max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('rooms', models.IntegerField()),
                ('workers', models.IntegerField()),
            ],
        ),
    ]
