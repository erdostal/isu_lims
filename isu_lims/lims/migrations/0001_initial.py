# Generated by Django 2.1.5 on 2019-02-22 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, choices=[('W', 'Wild'), ('D', 'Domesticated'), ('L', 'Landrace'), ('U', 'Unknown')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genome', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Genera',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('startdate', models.DateField(auto_now_add=True, null=True)),
                ('enddate', models.DateField(auto_now_add=True, null=True)),
                ('url', models.URLField(blank=True)),
                ('grant', models.TextField(blank=True)),
                ('lead', models.CharField(blank=True, max_length=100)),
                ('projecturl', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DNA'), ('R', 'RNA'), ('P', 'Protein'), ('E', 'Epigenetic'), ('O', 'Other')], max_length=1)),
                ('accession', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Accession')),
                ('plant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeedPacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('quantity', models.IntegerField(default=0)),
                ('datecollected', models.DateField(blank=True)),
                ('accession', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Accession')),
                ('parenta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='offspringa', to='lims.Plant')),
                ('parentb', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='offspringb', to='lims.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(blank=True, max_length=200)),
                ('genome', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Genome')),
            ],
            options={
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Subgenus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgenus', models.CharField(blank=True, max_length=200)),
                ('genus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Genus')),
            ],
            options={
                'verbose_name_plural': 'SubGenera',
            },
        ),
        migrations.AddField(
            model_name='seed',
            name='seed_packet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.SeedPacket'),
        ),
        migrations.AddField(
            model_name='plant',
            name='fromseed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Seed'),
        ),
        migrations.AddField(
            model_name='genome',
            name='subgenus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Subgenus'),
        ),
        migrations.AddField(
            model_name='accession',
            name='species',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lims.Species'),
        ),
    ]
