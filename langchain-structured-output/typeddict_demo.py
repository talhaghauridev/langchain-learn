from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "Talha Ghauri", "age": 18}

print(new_person)
