from django.db import models


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()  # 不限制长度
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 嵌套了Meta 类。Meta 存储用于管理模型的额外信息，在这里，它让我们能够设置一个特殊属性
        # 让Django在需要时使用Entries来表示多个条目。如果没有这个类
        # Django将使用Entrys来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text
