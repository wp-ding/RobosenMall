
from toolset.classproperty import classproperty


class AddressFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "title": True,
            "receiver": True,
            "province": True,
            "city": True,
            "district": True,
            "place": True,
            "mobile": True,
            "tel": True,
            "isDefault": True,
            "user": True,
        }
