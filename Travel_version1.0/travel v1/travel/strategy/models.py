from django.db import models
from user.models import User

# 攻略
class Strategy(models.Model):
    title = models.CharField('标题', max_length=50)
    cover_img = models.ImageField(upload_to='strategyImg', null=True)
    browse_nums = models.IntegerField('浏览数')
    collection = models.IntegerField('收藏数')
    good = models.IntegerField('赞')
    content = models.TextField()
    comments = models.IntegerField('评论数')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'strategy'

# 攻略评论
class StrategyComment(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('内容')
    good = models.IntegerField('赞')
    send_time = models.DateTimeField('发送时间', auto_now_add=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'strategycomment'

# 回复
class StrategyReply(models.Model):
    comment = models.ForeignKey(StrategyComment, on_delete=models.CASCADE, related_name='strategycomment_id')     # 评论id
    content= models.TextField('内容')
    good = models.IntegerField('赞')
    replyuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='strategycomment_replay')         # 回复用户id
    touser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='strategycomment_to')            # 目标用户id
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'strategyreply'

# 图片类型
class PictureType(models.Model):
    # (1  景点图片, 2  美食图片, 3  攻略图片, 4  用户上传, 5 酒店图片)
    picture_type = models.IntegerField(max_length=2)
    type_name = models.CharField(max_length=10)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'picturetype'

# 图片
class Picture(models.Model):
    picturetype = models.ForeignKey(PictureType, on_delete=models.CASCADE)
    picture_path = models.ImageField(upload_to='travel')
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'picture'