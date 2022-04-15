from toolset.classproperty import classproperty


class QAFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "question": True,
            "answer": True,
            "inactive": True,
            "creator": True,
            "created": True,
        }