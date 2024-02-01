import random


class Camp:
    def __init__(self, capacity):
        self._capacity = capacity

        self._persons = []

    def add_person(self, person):
        if len(self._persons) >= self._capacity:
            raise Exception("Camp is full")
        self._persons.append(person)

    def remove_person(self, person):
        self._persons.delete(person)

    def print_persons(self):
        for person in self._persons:
            print(person)

    def __getitem__(self, index):
        return self._persons[index]


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "Name: {}, Age: {}". format(self._name,
                                           self._age)

    def __call__(self):
        print("Please don't call me, I am not a function")


class Kadett(Person):
    def __init__(self, grade, *args):
        super().__init__(*args)
        self._grade = grade

    def __str__(self):
        return "Name: {}, Age: {}, Grade: {}". format(self._name,
                                                      self._age,
                                                      self._grade)



camp = Camp(10)

for i in range(5):
    person = Person(chr(i+65), random.randint(20, 40))

    camp.add_person(person)

for i in range(5):
    kadett = Kadett(chr(i+65), random.randint(20, 40), f"G_{i}")

    camp.add_person(kadett)

camp.print_persons()
print()

first_person = camp[0]
print(first_person)
first_person()

camp.add_person(Person("ohno", 40))
