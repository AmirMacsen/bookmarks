from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="出生日期")
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, verbose_name="头像")

    class Meta:
        verbose_name_plural = "用户档案"

    def __str__(self):
        return f"Profiles for user {self.user.username}"


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name="rel_from_set",
                                  on_delete=models.CASCADE)

    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"


# 动态添加following字段给用户模型
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False))