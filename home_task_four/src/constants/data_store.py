class DataStore:
    _instance = None
    _data = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def set_data(cls, key, value):
        cls._data[key] = value

    @classmethod
    def get_data(cls, key):
        return cls._data.get(key)
