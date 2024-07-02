# Generated by Django 5.0.6 on 2024-07-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhol', '0007_alter_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('community', '커뮤니티'), ('group-buying', '공구'), ('agency-document', '대행, 서류작성'), ('info', '정보')], max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(choices=[('intern', '해외취업'), ('language-study', '어학연수'), ('working-holiday', '워킹홀리데이')], max_length=15, unique=True),
        ),
    ]
