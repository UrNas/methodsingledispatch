"""
modified singledispatch decorator for class methods
"""
from functools import wraps
from weakref import WeakKeyDictionary
from types import MappingProxyType


def method_single_dispatch(func):
    registry = WeakKeyDictionary()

    def register(cls, decorated=None):
        if decorated is None:
            return lambda f: register(cls, f)
        registry[cls] = decorated
        return decorated

    def dispatch(cls):
        return registry.get(cls)

    @wraps(func)
    def inner(*args, **kwargs):
        return dispatch(args[1].__class__)(*args)

    inner.register = register
    inner.registry = MappingProxyType(registry)

    return inner
