"""A record of fields"""

class Namespace:
    """A namespace!"""

    def __init__(self, *args, **kwargs):
        """Initialize Me"""
        self.__dict__.update(kwargs)
        super().__init(*args, **kwargs)


class Record:
    """A Record of fields"""

    def __init__(self, *args, **kwargs):
        """Initialize Me!"""
        self.__field_names = tuple(kwargs.keys())
        self.__dict__.update(kwargs)

    @property
    def fields(self):
        """Only initialized fields."""
        return self.__field_names

    def __str__(self):
        """String representation."""
        return self.__reprt__()

    def __len__(self):
        """Record can be considered as an iterable."""
        return len(self.__field_names)

    def __repr__(self):
        """Represenet self."""
        return\
            "Record[\n"\
            + '\n'.join(
                "\t{}: {}".format(field, getattr(self, field))
                for field in self.__field_names
            ) + "]\n"

    @property
    def as_dict(self):
        """..."""
        return {
            field: getattr(self, field)
            for field in self.__field_names}

    @property
    def values(self):
        """values of the fields"""
        return self.as_dict.values()

    @property
    def keys(self):
        """keys of the fields"""
        return self.as_dict.keys()

    def __contains__(self, key):
        """Record is a container"""
        return hasattr(self, key)

    def get(self, key, default=None):
        """Record can be a dict"""
        return getattr(self, key, default)

    def __call__(self, key, default=None):
        """Record can also be a function!"""
        return self.get(key, default)

    def plus(self,
            *args, **kwargs):
        """Add another field"""
        r_dict = self.as_dict
        r_dict.update(kwargs)
        return Record(**r_dict)


            
