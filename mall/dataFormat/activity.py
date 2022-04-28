
from toolset.classproperty import classproperty


class ActivityFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "title": True,
            "content": True,
            "coverImage": True,
            "start": True,
            "end": True,
            "inactive": True,
            "discount": True,
            "coupon": True,
            "status": True,
            "creator": True,
            "created": True,
        }