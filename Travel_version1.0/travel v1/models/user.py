from django.db import models

# 用户
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField('用户名',max_length=8 ,unique=True)
    password = models.CharField('密码', max_length=20)
    email = models.EmailField('邮箱')
    phone = models.CharField('手机号', max_length=11)
    info = models.CharField(max_length=150,verbose_name='个人简介')
    avatar = models.ImageField(upload_to='avatar', null=True)       # 用户头像
    created_date = models.DateField('注册日期', auto_now_add=True)

    class Meta:
        db_table = 'user'

# 关注,被关注
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')    # 关注者（粉丝）
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow')    # 被关注

    class Meta:
        db_table = 'follow'

