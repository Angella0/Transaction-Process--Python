class Student:
    school = "AkiraChix"

    def __init__(self,first_name,last_name,age):
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age 

 

    def speak(self):
        return f"Hello class, my name is {self.first_name}"
    def year_of_birth(self):
        return f"Hello {self.first_name} you were born in {2021-self.age}"

    def greet(self):
        return f" Hello {self.last_name} welcome to {self.school}"

    def initials(self):
        return f" Hello your initials are {self.first_name[0]} {self.last_name[0]}"
