from django.db import models

# Create your models here.
class ReportContent(models.Model):

    report = models.TextField(blank=True, null=True)
    request_type = models.CharField('请求类型',max_length=1,default='E')
    input_time = models.DateTimeField('输入时间', auto_now_add=True)

    class Meta:
        db_table = 'content'
        verbose_name = '报告内容'
        verbose_name_plural = '报告内容'

    def __str__(self):
        return 'report content %s' % (self.report)

class RespondContent(models.Model):

    responds = models.TextField(blank=True, null=True)
    request_type = models.CharField('请求类型',max_length=1,default='E')
    output_time = models.DateTimeField('输入时间', auto_now_add=True)

    class Meta:
        db_table = 'reply'
        verbose_name = '响应内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'reply content %s' % (self.responds)
