# Generated by Django 4.2.3 on 2023-07-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_tempuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType1', models.CharField(choices=[('option1', '계획형'), ('option2', '즉흥형')], default='option1', max_length=15)),
                ('userType2', models.CharField(choices=[('option3', '바쁘게 움직이는 여행'), ('option4', '오직 휴식을 위한 여행')], default='option3', max_length=15)),
                ('userType3', models.CharField(choices=[('option5', '사진 찍는 거 좋아요'), ('option6', '사진 찍는 거 싫어요')], default='option5', max_length=15)),
                ('userType4', models.CharField(choices=[('option7', '번화가'), ('option8', '자연, 시골')], default='option7', max_length=15)),
            ],
            options={
                'verbose_name': 'Model_tempUser2',
                'verbose_name_plural': 'Model_tempUser2',
                'db_table': 'tempUser2',
            },
        ),
    ]
