import random

if __name__ == "__main__":
    import sys
    import os

    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_DIR not in sys.path:
        sys.path.insert(0, PROJECT_DIR)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RobosenMall.settings.dev')

    import django
    django.setup()

    from mall.models import Product, ProductInfo
    from toolset.utils import generateCode
    i = 0
    while i <= 50:

        name = generateCode(5)
        category = random.randint(1,2)
        subCategory = random.choice(['k1pro', 'k1'])
        color = random.choice(['red', 'green', 'black', 'white'])
        price = random.randint(3000, 5000)
        description = random.choice(['君不见黄河之水天上来，奔流到海不复回。', '君不见高堂明镜悲白发，朝如青丝暮成雪', ''])
        product = Product.objects.create(
            name=name,
            category=category,
            subCategory=subCategory,
            color=color,
            price=price,
            description=description,
        )

        size = "{}*{}*{}mm".format(random.randint(100,200), random.randint(10,60), random.randint(200,600))
        weight = "{}kg".format(round(random.random(), 3))
        material = "{}外壳， {}合金".format(generateCode(2), generateCode(3))
        servo = "{}自由度，(頭：{}， 腳{})".format(random.randint(10,25), random.randint(10,25), random.randint(10,25))
        communicationMethod = "藍牙{}".format(random.randint(1,5))
        controlMethod = random.choice(['手机app', '语音控制', '手机或语音控制'])
        peripheralInterface = random.choice(['DC充电', 'Type-c接口'])
        batteryType = random.choice(['锂电池', '常规石墨电池'])
        batteryCapacity = random.choice(['{}mah锂电池'.format(random.randint(100,200)), '常规石墨电池'])
        powerAdapter = "输入{}v-{}v-{}hz".format(random.randint(10,25), random.randint(10,25), random.randint(10,25))

        mobileControl = random.choice(['ios', 'android', 'ios/android'])
        voiceControl = "{}命令".format(random.randint(100,200))
        programmable = "{}编程选项".format(random.randint(100,200))
        microchip = "{}芯片".format(random.randint(100,200))
        mic = '内置麦克风'
        loudspeaker = '扬声器'
        addOns = '提供维修部件等'

        ProductInfo.objects.create(
            productId=product.id,
            size=size,
            weight=weight,
            material=material,
            servo=servo,
            communicationMethod=communicationMethod,
            controlMethod=controlMethod,
            peripheralInterface=peripheralInterface,
            batteryType=batteryType,
            batteryCapacity=batteryCapacity,
            powerAdapter=powerAdapter,
            mobileControl=mobileControl,
            voiceControl=voiceControl,
            programmable=programmable,
            microchip=microchip,
            mic=mic,
            loudspeaker=loudspeaker,
            addOns=addOns,
        )

        i+=1