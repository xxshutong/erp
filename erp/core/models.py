# coding: utf-8
from datetime import timedelta, tzinfo
from django.db import models

#初始化migration ./manage.py schemamigration core --initial
#生成migration ./manage.py schemamigration core --auto
#应用migration ./manage.py migrate core
from erp.settings import DATETIME_FORMAT
import pytz


class Configuration(models.Model):
    """
    配置
    """

    class Meta:
        verbose_name_plural = u'配置信息，只有一条记录'
        verbose_name = u'配置信息'

    notify_time_interval = models.IntegerField('提醒时间间隔（单位天）', blank=False, null=False)
    page_size = models.IntegerField('每页记录条数', default=10);


    def __unicode__(self):
        return u'配置信息'


class Type(models.Model):
    """
    机器种类
    """

    class Meta:
        verbose_name_plural = u'基础表-机器种类列表'
        verbose_name = u'机器种类'

    name = models.CharField('种类名', max_length=50, blank=False)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    """
    产品种类
    """

    class Meta:
        verbose_name_plural = u'基础表-产品种类列表'
        verbose_name = u'产品种类'

    name = models.CharField('产品名', max_length=255, blank=False)

    def __unicode__(self):
        return self.name


class Material(models.Model):
    """
    原料
    """

    class Meta:
        verbose_name_plural = u'基础表-原料列表'
        verbose_name = u'原料'

    name = models.CharField('原料成份', max_length=255, blank=False)

    def __unicode__(self):
        return self.name


class TouWen(models.Model):
    """
    头纹
    """

    class Meta:
        verbose_name_plural = u'基础表-头纹列表'
        verbose_name = u'头纹'

    name = models.CharField('头纹名称', max_length=255, blank=False)

    def __unicode__(self):
        return self.name


class Machine(models.Model):
    """
    机器设备
    """

    class Meta:
        verbose_name_plural = u'1-织机设备列表'
        verbose_name = u'织机设备'

    no = models.IntegerField('机号', blank=False, null=False)
    type = models.ForeignKey(Type, name='type', verbose_name="种类")
    product = models.ForeignKey(Product, name='product', verbose_name='产品名称')
    material = models.ForeignKey(Material, name='material', verbose_name='原料成份')
    tou_wen = models.ForeignKey(TouWen, name='tou_wen', verbose_name='头纹')
    length = models.FloatField('经轴米数')
    length_available = models.FloatField('经轴可织米数', null=True, blank=True)
    wei_mi = models.FloatField('纬密')
    speed = models.IntegerField('车速')
    efficiency = models.FloatField('效率', blank=True, null=True)
    take_up_rate = models.FloatField('织缩率', blank=True, null=True)
    daily_output_estimated = models.IntegerField('预计日产量', blank=True, null=True)
    # daily_output_actual = models.IntegerField('实际日产量', blank=True, null=True)
    start_time = models.DateTimeField('上机时间', blank=False)
    # end_time_estimated = models.DateTimeField('预计结束时间', blank=True, null=True)
    # end_time_actual = models.DateTimeField('实际结束时间', blank=True, null=True)
    remark = models.CharField('备注', max_length=10000, blank=True, null=True)

    def __unicode__(self):
        return u'机号-%s' % self.no

    def end_time_estimated(self):
        if self.speed and self.wei_mi and self.efficiency and self.length_available and self.start_time:
            interval = self.length_available / (self.speed / self.wei_mi * 60 / 100 * self.efficiency)
            return self.start_time + timedelta(hours=interval)
        return None

    def end_time_estimated_format(self):
        temp = self.end_time_estimated().astimezone(pytz.timezone('Asia/Shanghai'))
        if temp is not None:
            return temp.strftime("%Y年%m月%d日%H时")
        return None


    end_time_estimated_format.short_description = u'预计结束时间'
    end_time_estimated_display = property(end_time_estimated)
