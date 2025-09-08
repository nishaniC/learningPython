def log_getattr(cls):
    original_getattr = cls.__getattr__ if hasattr(cls, '__getattr__') else lambda self, name: f"'{name}' not found"

    def new_getattr(self, name):
        print(f"Accessing missing attribute: {name}")
        return original_getattr(self, name)  # Fallback to original behavior

    cls.__getattr__ = new_getattr
    return cls

@log_getattr
class Demo:
    def __init__(self, value):
        self.value = value

obj = Demo(42)
print(obj.value)  # Normal attribute access
print(obj.undefined_attr)  # Triggers __getattr__
