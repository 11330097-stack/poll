from django.db import models

# Create your models here.

class polll(models.Model):
    subject =models.CharField("投票主題", max_length=64)
    desc =models.TextField("說明")
    created =models .DateField("建立日期")


class Option (models.Model):
    title =models.CharField("選項文字", max_length=64)
    votes = models.IntegerChoices("票數",default =0)
    votes = models.IntegerChoices("投票主題編號")