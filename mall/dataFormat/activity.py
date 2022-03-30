
from toolset.classproperty import classproperty


class ActivityFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "title": True,
        }