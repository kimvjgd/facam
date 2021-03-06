from django.db import models

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                 verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registerer_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='동록시간')
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스크캠퍼스 사용자'