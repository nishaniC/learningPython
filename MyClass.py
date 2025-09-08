class MyClass:
    def __init__(self, attribute):
        self.__attribute = attribute

    def __str__(self):
        return f"{self.__attribute}:{self.__attribute}"

# Example usage
obj = MyClass("example")
print(obj)  # Output: MyClass with attribute: example
