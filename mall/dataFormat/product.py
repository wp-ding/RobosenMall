
from toolset.classproperty import classproperty


class ProductFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "name": True,
            "category": True,
            "subCategory": True,
            "color": True,
            "price": True,
            "description": True,
            "size": True,
            "weight": True,
            "humanForm": True,
            "carForm": True,
            "material": True,
            "servo": True,
            "communicationMethod": True,
            "controlMethod": True,
            "peripheralInterface": True,
            "batteryType": True,
            "batteryCapacity": True,
            "powerAdapter": True,
            "mobileControl": True,
            "voiceControl": True,
            "programmable": True,
            "microchip": True,
            "mic": True,
            "loudspeaker": True,
            "addOns": True,
            # "pictures": True,

            "creator": True,
            "created": True,
        }