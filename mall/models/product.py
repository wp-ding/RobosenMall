from django.db import models


class Product(models.Model):
    original = 1
    jointly = 2

    name = models.CharField(max_length=64)
    category = models.IntegerField(default=1)
    subCategory = models.CharField(max_length=32, null=True)
    color = models.CharField(max_length=32, null=True)
    price = models.BigIntegerField(null=True)
    description = models.TextField(null=True)
    inactive = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    creatorId = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)


class ProductInfo(models.Model):
    productId = models.IntegerField(null=True)
    size = models.CharField(max_length=32, null=True)
    weight = models.CharField(max_length=32, null=True)
    humanForm = models.CharField(max_length=32, null=True)
    carForm = models.CharField(max_length=32, null=True)
    material = models.CharField(max_length=32, null=True)  # 材质
    servo = models.CharField(max_length=64, null=True)  # 舵机
    communicationMethod = models.CharField(max_length=64, null=True)  # 通讯方式
    controlMethod = models.CharField(max_length=64, null=True)  # 控制方式
    peripheralInterface = models.CharField(max_length=64, null=True)  # 外围接口
    batteryType = models.CharField(max_length=32, null=True)  # 电池类型
    batteryCapacity = models.CharField(max_length=32, null=True)  # 电池容量
    powerAdapter = models.CharField(max_length=32, null=True)  # 电源适配器

    mobileControl = models.CharField(max_length=32, null=True)  # 移动应用控制
    voiceControl = models.CharField(max_length=32, null=True)  # 语音控制
    programmable = models.CharField(max_length=32, null=True)  # 可编程
    microchip = models.CharField(max_length=32, null=True)  # 微芯片
    mic = models.CharField(max_length=32, null=True)  # 麦克风
    loudspeaker = models.CharField(max_length=32, null=True)  # 扬声器
    addOns = models.CharField(max_length=64, null=True)  # 附加功能


class ProductPicture(models.Model):
    productId = models.IntegerField()
    picture = models.CharField(max_length=256, null=True)
    index = models.IntegerField()


