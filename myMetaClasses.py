import time

class TrackingMeta(type):
    instantiated_classes = []  # Keeps track of class creation order

    def __new__(cls, name, bases, class_dict):
        class_dict['instantiation_time'] = time.time()  # Store timestamp
        class_dict['get_instantiation_time'] = lambda self: self.instantiation_time  # Add retrieval method
        
        new_class = super().__new__(cls, name, bases, class_dict)
        cls.instantiated_classes.append(name)  # Log class instantiation order
        
        print(f"Class '{name}' created at {class_dict['instantiation_time']}")  # Debug info
        return new_class

# Example legacy classes using the metaclass
class LegacyClassA(metaclass=TrackingMeta):
    pass

class LegacyClassB(metaclass=TrackingMeta):
    pass

class LegacyClassC(metaclass=TrackingMeta):
    pass

# Instantiate objects
a = LegacyClassA()
b = LegacyClassB()
c = LegacyClassC()

# Access instantiation times
print(f"LegacyClassA instantiation time: {a.get_instantiation_time()}")
print(f"LegacyClassB instantiation time: {b.get_instantiation_time()}")
print(f"LegacyClassC instantiation time: {c.get_instantiation_time()}")

# List instantiated classes in order
print(f"Instantiation order: {TrackingMeta.instantiated_classes}")

import time

class TrackingMeta(type):
    instantiated_classes = []  # Keeps track of class creation order

    def __new__(cls, name, bases, class_dict):
        class_dict['instantiation_time'] = time.time()  # Store timestamp

        # Define method explicitly instead of using lambda
        def get_instantiation_time(self):
            return self.instantiation_time
        
        class_dict['get_instantiation_time'] = get_instantiation_time  # Add method
        
        new_class = super().__new__(cls, name, bases, class_dict)
        cls.instantiated_classes.append(name)  # Log class instantiation order
        
        print(f"Class '{name}' created at {class_dict['instantiation_time']}")  # Debug info
        return new_class

# Example legacy classes using the metaclass
class LegacyClassA(metaclass=TrackingMeta):
    pass

class LegacyClassB(metaclass=TrackingMeta):
    pass

class LegacyClassC(metaclass=TrackingMeta):
    pass

# Instantiate objects
a = LegacyClassA()
b = LegacyClassB()
c = LegacyClassC()

# Access instantiation times
print(f"LegacyClassA instantiation time: {a.get_instantiation_time()}")
print(f"LegacyClassB instantiation time: {b.get_instantiation_time()}")
print(f"LegacyClassC instantiation time: {c.get_instantiation_time()}")

# List instantiated classes in order
print(f"Instantiation order: {TrackingMeta.instantiated_classes}")
