class Person:
    def __init__(self, name: str, age: int, birth_year: int, gender=None):
        self.name = name  # Person has a name // has a relation with instance
        self.__age = age
        self.__birth_year = birth_year  # Private variable / Data encapsulation
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry, Name can't have number")
            return
        self.name = new_name

    def get_birth_year(self):
        return self.__birth_year

    def __has_any_number(self, string):  # private method. It can't be callable by outside of this class
        # If anyone directly access the value then we can't check the validity of
        # that new data. So that we use method for accessing instance
        return "0" in string

    def get_summery(self):
        return f"Name: {self.name}, Age: {self.__age}, BirthYear: {self.__birth_year}, Gender: {self.gender}"


person1 = Person("Niloy", 22, 1999)
person2 = Person("Akib", 24, 1997)

print(person1.name)  # Access directly without function
print(person2.get_name())  # Access with function

person2.set_name("Akib Bin Khodar Khashi")  # override the value of name using set
print(person2.get_summery())

person1.name = "Niloy Biswas"  # Access variable directly / for stop is use private variable
print(person1.get_name())

person1.set_name("00NIloy")
print(person1.get_name())

person_list = [Person("Mahi", 23, 1998),
               Person("Riaz", 23, 1998, "Male"),
               Person("Moon", 50, 1970, "Male")]

for person in person_list:
    if person.get_birth_year() >= 1990:
        print(person.get_summery())


class Student(Person):  # Inheritance / Person is the super class
    # Student is a Person / is a relation between sub and supper class
    def __init__(self, name: str, age: int, birth_year: int, student_id: str):
        super().__init__(name, age, birth_year)
        self.student_id = student_id

    def get_summery(self):
        return f"Name: {self.get_name()}, BirthYear: {self.get_birth_year()}, ID: {self.student_id}"


student1 = Student("Tomi", 25, 1995, "171-35-239")
print(student1.get_summery())
student1.set_name("Tanvir")
print(student1.get_summery())


class Teacher(Person):  # Teacher is a Person
    def __init__(self, name: str, age: int, birth_year: int, dept: str):
        super().__init__(name, age, birth_year)
        self.department = dept


all_person_list = [
    Person("Niloy", 22, 1999),
    Student("Taz", 26, 1994, "171-35-241"),
    Teacher("BIkash", 30, 1990, "SWE")
]

for p in all_person_list:
    print(p.get_summery())
