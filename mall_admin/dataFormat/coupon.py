from toolset.classproperty import classproperty


class CouponFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "code": True,
            "title": True,
            "product": True,
            "amount": True,
            "threshold": True,
            "expiration": True,
            "closed": True,
            "auto": True,
            "limit": True,
            "created": True,
            "creator": True,
        }