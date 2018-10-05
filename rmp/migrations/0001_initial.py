# Generated by Django 2.1.1 on 2018-10-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccChem',
            fields=[
                ('accchem_id', models.IntegerField(help_text='A unique ID for each accident chemical record.', primary_key=True, serialize=False, verbose_name='Accident Chemical Record ID')),
                ('accident_id', models.IntegerField(help_text='The unique ID for each accident record')),
                ('chemical_id', models.IntegerField(help_text='The identifying ID for a particular chemical released in an accident.')),
                ('quantity_lbs', models.IntegerField(help_text='The amount of the substance released in the accident, in pounds, to two significant digits.', verbose_name='Amount Released (lbs)')),
                ('percent_weight', models.DecimalField(decimal_places=2, help_text='The percent weight of a chemical within a mixture released in an accident.', max_digits=5, null=True, verbose_name='Percent Weight (Within Mixture)')),
                ('num_acc_flam', models.IntegerField(help_text='The number of listed flammable component chemicals for this chemical record.', null=True, verbose_name='Number of Flammable Components')),
                ('cas', models.CharField(help_text='The identifying CAS number for a chemical.', max_length=9, verbose_name='CAS number')),
                ('chemical_type', models.CharField(choices=[('T', 'toxic'), ('F', 'flammable')], help_text='"The type of chemical.', max_length=1)),
            ],
            options={
                'db_table': 'rmp_acc_chem',
            },
        ),
        migrations.CreateModel(
            name='AccFlam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flammixchem_id', models.IntegerField(help_text='A unique ID for each flammable chemical record.', verbose_name='Flammable Chemical ID')),
                ('accchem_id', models.IntegerField(help_text='A unique ID for each accident chemical record.', verbose_name='Accident Chemical Record ID')),
                ('chemical_id', models.IntegerField(help_text='The identifying ID for a particular flammable chemical released in an accident.', verbose_name='Chemical ID')),
            ],
            options={
                'db_table': 'rmp_acc_flam',
            },
        ),
        migrations.CreateModel(
            name='ChemCd',
            fields=[
                ('chemical_id', models.IntegerField(help_text="RMP's unique identifier of a chemical substance.", primary_key=True, serialize=False)),
                ('chemical_name', models.CharField(help_text='Chemical substance name.', max_length=92)),
                ('cas2', models.CharField(blank=True, help_text='Chemical Abstracts Service (CAS) registry number (is 2 meaningful?)', max_length=10)),
                ('threshold', models.IntegerField(help_text='Threshold above which the chemical is regulated???')),
                ('chemical_type', models.CharField(blank=True, choices=[('T', 'toxic'), ('F', 'flammable')], help_text='"The type of chemical (T=toxic, F=Flammable).', max_length=1)),
                ('cbi_flag', models.BooleanField(help_text='Indicates whether this record contained Confidential Business Information (CBI) which has been erased by EPA from the public version of the data.')),
                ('chemical_owner', models.CharField(blank=True, max_length=3)),
            ],
            options={
                'db_table': 'rmp_chem_cd',
            },
        ),
        migrations.CreateModel(
            name='DeregCd',
            fields=[
                ('dereg', models.IntegerField(help_text='Unique identifier of the de-regulation reason.', primary_key=True, serialize=False)),
                ('dereg_tr', models.CharField(help_text='Full description of the de-regulation reason.', max_length=62)),
            ],
            options={
                'db_table': 'rmp_dereg_cd',
            },
        ),
        migrations.CreateModel(
            name='DochanCd',
            fields=[
                ('dochan', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('dochan_tr', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'rmp_dochan_cd',
            },
        ),
        migrations.CreateModel(
            name='DoctypCd',
            fields=[
                ('doctyp', models.CharField(help_text='Unique identifier of the document type.', max_length=1, primary_key=True, serialize=False)),
                ('doctyp_tr', models.CharField(help_text='Full description of the document type.', max_length=30)),
            ],
            options={
                'db_table': 'rmp_doctyp_cd',
            },
        ),
        migrations.CreateModel(
            name='EventsCd',
            fields=[
                ('events', models.CharField(help_text='Unique identifier of the event type.', max_length=1, primary_key=True, serialize=False)),
                ('events_tr', models.CharField(help_text='Full description of the event type.', max_length=40)),
            ],
            options={
                'db_table': 'rmp_events_cd',
            },
        ),
        migrations.CreateModel(
            name='ExecSumLen',
            fields=[
                ('rmp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('byte_count', models.IntegerField()),
                ('suspect_count', models.IntegerField()),
                ('line_count', models.IntegerField()),
                ('edited_yn', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'rmp_exec_sum_len',
            },
        ),
        migrations.CreateModel(
            name='LldescCd',
            fields=[
                ('lldesc', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('lldesc_tr', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'rmp_lldesc_cd',
            },
        ),
        migrations.CreateModel(
            name='LlmethCd',
            fields=[
                ('primary_key', models.IntegerField(primary_key=True, serialize=False)),
                ('llmeth', models.CharField(max_length=2)),
                ('llmeth_tr', models.CharField(max_length=83)),
            ],
            options={
                'db_table': 'rmp_llmeth_cd',
            },
        ),
        migrations.CreateModel(
            name='PhysCd',
            fields=[
                ('phys', models.CharField(help_text='Unique identifier of the physical state.', max_length=1, primary_key=True, serialize=False)),
                ('phys_tr', models.CharField(help_text='Full description of the physical state.', max_length=30)),
            ],
            options={
                'db_table': 'rmp_phys_cd',
            },
        ),
        migrations.CreateModel(
            name='Prevent2Chem',
            fields=[
                ('primary_key', models.IntegerField(primary_key=True, serialize=False)),
                ('prevent_2_id', models.IntegerField()),
                ('procchem_id', models.IntegerField()),
            ],
            options={
                'db_table': 'rmp_prevent_2_chem',
            },
        ),
        migrations.CreateModel(
            name='Prevent3Chem',
            fields=[
                ('primary_key', models.IntegerField(primary_key=True, serialize=False)),
                ('prevent_3_id', models.IntegerField()),
                ('procchem_id', models.IntegerField()),
            ],
            options={
                'db_table': 'rmp_prevent_3_chem',
            },
        ),
        migrations.CreateModel(
            name='ProcChem',
            fields=[
                ('procchem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('process_id', models.IntegerField()),
                ('chemical_id', models.IntegerField()),
                ('quantity_lbs', models.IntegerField()),
                ('cbi_flag', models.BooleanField()),
                ('num_alt_flam', models.IntegerField()),
                ('num_alt_tox', models.IntegerField()),
                ('num_prevent_2_chem', models.IntegerField()),
                ('num_prevent_3_chem', models.IntegerField()),
                ('num_proc_flam', models.IntegerField()),
                ('num_worst_flam', models.IntegerField()),
                ('num_worst_tox', models.IntegerField()),
                ('cas', models.IntegerField()),
                ('chemical_type', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'rmp_proc_chem',
            },
        ),
        migrations.CreateModel(
            name='ProcFlam',
            fields=[
                ('flammixchem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('procchem_id', models.IntegerField()),
                ('chemical_id', models.IntegerField()),
            ],
            options={
                'db_table': 'rmp_proc_flam',
            },
        ),
        migrations.CreateModel(
            name='ProcNaics',
            fields=[
                ('procnaics_id', models.IntegerField(primary_key=True, serialize=False)),
                ('process_id', models.IntegerField()),
                ('naics', models.IntegerField()),
                ('num_prevent_2', models.IntegerField()),
                ('num_prevent_3', models.IntegerField()),
            ],
            options={
                'db_table': 'rmp_proc_naics',
            },
        ),
        migrations.CreateModel(
            name='RejectCd',
            fields=[
                ('reject', models.CharField(help_text='Unique identifier of the rejection reason.', max_length=1, primary_key=True, serialize=False)),
                ('reject_tr', models.CharField(help_text='Full description of the rejection reason.', max_length=59)),
            ],
            options={
                'db_table': 'rmp_reject_cd',
            },
        ),
        migrations.CreateModel(
            name='ScenCd',
            fields=[
                ('scen', models.CharField(help_text='Unique identifier of the scenario.', max_length=1, primary_key=True, serialize=False)),
                ('scen_tr', models.CharField(help_text='Full description of the scenario.', max_length=27)),
            ],
            options={
                'db_table': 'rmp_scen_cd',
            },
        ),
        migrations.CreateModel(
            name='SubmitCd',
            fields=[
                ('submit', models.CharField(help_text='Unique identifier of the submission reason.', max_length=3, primary_key=True, serialize=False)),
                ('submit_tr', models.CharField(help_text='Full description of the submission reason.', max_length=101)),
            ],
            options={
                'db_table': 'rmp_submit_cd',
            },
        ),
        migrations.CreateModel(
            name='Tbls6Accidentchemicals',
            fields=[
                ('accchem_id', models.IntegerField(help_text='A unique ID for each accident chemical record.', primary_key=True, serialize=False, verbose_name='Accident Chemical Record ID')),
                ('accident_id', models.IntegerField(help_text='The unique ID for each accident record')),
                ('chemical_id', models.IntegerField(help_text='The identifying ID for a particular chemical released in an accident.')),
                ('quantity_lbs', models.IntegerField(help_text='The amount of the substance released in the accident, in pounds, to two significant digits.', verbose_name='Amount Released (lbs)')),
                ('percent_weight', models.DecimalField(decimal_places=2, help_text='The percent weight of a chemical within a mixture released in an accident.', max_digits=5, null=True, verbose_name='Percent Weight (Within Mixture)')),
            ],
            options={
                'db_table': 'tblS6AccidentChemicals',
            },
        ),
        migrations.CreateModel(
            name='TopoCd',
            fields=[
                ('topo', models.CharField(help_text='Unique identifier of the topography type.', max_length=1, primary_key=True, serialize=False)),
                ('topo_tr', models.CharField(help_text='Full description of the topography type.', max_length=5)),
            ],
            options={
                'db_table': 'rmp_topo_cd',
            },
        ),
        migrations.CreateModel(
            name='WindCd',
            fields=[
                ('wind', models.CharField(help_text='Unique identifier of the wind speed measurement unit.', max_length=1, primary_key=True, serialize=False)),
                ('wind_tr', models.CharField(help_text='Full description of the wind speed measurement unit.', max_length=13)),
            ],
            options={
                'db_table': 'rmp_wind_cd',
            },
        ),
    ]
