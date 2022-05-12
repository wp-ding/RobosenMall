
from toolset.classproperty import classproperty


class AreaFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "name": True,
            "parent": True,
        }
