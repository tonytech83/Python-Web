"""
Example how to make instance callable
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        pass


p = Person('John', 19)
