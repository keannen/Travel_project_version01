# Generated by Django 2.2.12 on 2020-07-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_type', models.IntegerField(max_length=2)),
                ('type_name', models.CharField(max_length=10)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'picturetype',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('cover_img', models.ImageField(null=True, upload_to='strategyImg')),
                ('browse_nums', models.IntegerField(verbose_name='浏览数')),
                ('collection', models.IntegerField(verbose_name='收藏数')),
                ('good', models.IntegerField(verbose_name='赞')),
                ('content', models.TextField()),
                ('comments', models.IntegerField(verbose_name='评论数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'strategy',
            },
        ),
        migrations.CreateModel(
            name='StrategyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('good', models.IntegerField(verbose_name='赞')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('is_delete', models.BooleanField(default=0)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Strategy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'strategycomment',
            },
        ),
        migrations.CreateModel(
            name='StrategyReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('good', models.IntegerField(verbose_name='赞')),
                ('is_delete', models.BooleanField(default=0)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategycomment_id', to='strategy.StrategyComment')),
                ('replyuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategycomment_replay', to='user.User')),
                ('touser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategycomment_to', to='user.User')),
            ],
            options={
                'db_table': 'strategyreply',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_path', models.ImageField(upload_to='travel')),
                ('is_delete', models.BooleanField(default=0)),
                ('picturetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.PictureType')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
    ]