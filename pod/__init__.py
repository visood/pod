"""Utilities for plain old data"""

class POD:
    """Plain Old Data"""
    def __init__(self, *args, **kargs):
        """Initialize Me"""
        raise TypeError(
            "Attempt to initialize a POD class.")
