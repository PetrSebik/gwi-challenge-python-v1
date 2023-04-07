# Generated by Django 4.0.4 on 2023-04-07 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinosaur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('eating_classification', models.CharField(blank=True, choices=[('herbivores', 'Herbivores'), ('omnivores', 'Omnivores'), ('carnivores', 'Carnivores')], default=None, max_length=10, null=True)),
                ('typical_colour', models.CharField(max_length=32)),
                ('period_lived', models.CharField(blank=True, choices=[('triassic', 'Triassic'), ('jurassic', 'Jurassic'), ('cretaceous', 'Cretaceous'), ('paleogene', 'Paleogene'), ('neogene', 'Neogene')], default=None, max_length=10, null=True)),
                ('average_size', models.CharField(choices=[('tiny', 'Tiny'), ('very_small', 'Very Small'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('very_large', 'Very Large')], default='medium', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DinosaurMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('dinosaur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='dinosaurs.dinosaur')),
            ],
        ),
        migrations.CreateModel(
            name='DinosaurLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinosaur_like', to=settings.AUTH_USER_MODEL)),
                ('dinosaur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='dinosaurs.dinosaur')),
            ],
        ),
    ]
