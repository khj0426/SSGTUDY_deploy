# Generated by Django 4.1 on 2022-08-19 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mypage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruituser',
            name='recruit_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruit_users', to='mypage.recruit'),
        ),
        migrations.AddField(
            model_name='recruituser',
            name='recruit_user_register',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruit_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recomment',
            name='recomment_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to='match.comment'),
        ),
        migrations.AddField(
            model_name='recomment',
            name='recomment_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_recruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mypage.recruit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
